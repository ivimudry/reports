# Generate Oshi welcome flow banner assets via OpenAI gpt-image-1.
#
# - Backgrounds: text-to-image (no reference)
# - Mascots: image-edit using the original mascot PNG + per-banner costume/pose prompt
# - Output is organized per banner section + GEO variant
#
# Run:
#   c:/Projects/REPORTS/.venv/Scripts/python.exe scripts/generate_banners.py
#
# Optional CLI flags:
#   --quality {low,medium,high}   (default: medium)
#   --only EMAIL_5_AU,EMAIL_1     (comma-separated section_variant filter)
#   --skip-bg / --skip-mascot     (generate only one of the two)
#   --dry-run                     (parse + plan + show prompts, no API calls)

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Force UTF-8 stdout for Cyrillic on Windows.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


# ---------------------------------------------------------------------------
# Paths & configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
DESCRIPTIONS_FILE = (
    REPO_ROOT / "тексти" / "оші" / "тексти" / "oshi welcome flow banner descriptions UA.txt"
)
MASCOT_REFERENCE = (
    REPO_ROOT / "тексти" / "оші" / "схеми та інше" / "IMG_2339 1.png"
)
OUTPUT_DIR = REPO_ROOT / "banners-output"
ENV_FILE = REPO_ROOT / ".env"

# Concurrency: small to stay friendly with rate limits.
MAX_WORKERS = 4

# Image sizes (gpt-image-1 supported: 1024x1024, 1024x1536, 1536x1024, auto).
BG_SIZE = "1536x1024"      # landscape background (banner is 600x300)
MASCOT_SIZE = "1024x1536"  # portrait, full-body mascot

# Cross-references: variant on the LEFT reuses outputs from variant on the RIGHT.
CROSS_REFERENCES = {
    "INAPP_5_DEFAULT_DE": "EMAIL_5_DEFAULT_DE",
    "INAPP_5_AU": "EMAIL_5_AU",
    "INAPP_5_CA": "EMAIL_5_CA",
}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class BannerVariant:
    section_id: str          # e.g. "EMAIL_1", "EMAIL_5"
    variant_id: str          # e.g. "ALL", "AU", "DEFAULT_DE"
    section_title: str       # raw section header for context
    variant_label: str       # raw variant label (e.g. "DEFAULT / DE | Elvis Frog TRUEWAYS")
    mascot_prompt: str
    background_prompt: str
    notes: list[str] = field(default_factory=list)

    @property
    def folder_name(self) -> str:
        if self.variant_id == "ALL":
            return self.section_id
        return f"{self.section_id}_{self.variant_id}"


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

SECTION_RE = re.compile(r"^=+\s*(.+?)\s*=+\s*$", re.MULTILINE)
VARIANT_RE = re.compile(r"^---\s*(.+?)\s*---\s*$", re.MULTILINE)
MASCOT_RE = re.compile(
    r"Маскот[^:\n]*:\s*(.+?)(?=\n\s*Фон[^:\n]*:|\Z)",
    re.DOTALL,
)
BACKGROUND_RE = re.compile(
    r"Фон[^:\n]*:\s*(.+?)\Z",
    re.DOTALL,
)


def slugify_section(title: str) -> str:
    # Pull a short id like "EMAIL_5" or "INAPP_1_2" from the section header.
    m = re.match(r"\s*(EMAIL|INAPP)\s*#?\s*([\d.]+)", title, re.IGNORECASE)
    if not m:
        # Fallback: take first two ASCII tokens.
        ascii_tokens = re.findall(r"[A-Za-z0-9]+", title)[:2]
        return "_".join(ascii_tokens).upper() or "SECTION"
    kind = m.group(1).upper()
    num = m.group(2).replace(".", "_")
    return f"{kind}_{num}"


def slugify_variant(label: str) -> str:
    # Extract GEO tokens from a variant header.
    # Examples: "DEFAULT / DE | Elvis Frog TRUEWAYS" -> "DEFAULT_DE"
    #           "AU | Big Bass Bonanza"             -> "AU"
    head = label.split("|", 1)[0]
    parts = re.split(r"[\s/]+", head.strip())
    geos = [p.upper() for p in parts if p.upper() in {"DEFAULT", "AU", "CA", "DE"}]
    if not geos:
        return "ALL"
    return "_".join(geos)


def parse_descriptions(text: str) -> list[BannerVariant]:
    # Split top-level sections by "==========" headers.
    matches = list(SECTION_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        sections.append((title, body))

    # We only care about banner sections (start with EMAIL or INAPP).
    variants: list[BannerVariant] = []
    for title, body in sections:
        if not re.match(r"^(EMAIL|INAPP)", title, re.IGNORECASE):
            continue
        section_id = slugify_section(title)

        # Find variant separators inside the body.
        var_matches = list(VARIANT_RE.finditer(body))
        if not var_matches:
            # Single, all-GEO variant.
            v = build_variant(
                section_id=section_id,
                variant_id="ALL",
                section_title=title,
                variant_label="",
                body=body,
            )
            if v:
                variants.append(v)
            continue

        for i, m in enumerate(var_matches):
            label = m.group(1).strip()
            v_start = m.end()
            v_end = var_matches[i + 1].start() if i + 1 < len(var_matches) else len(body)
            v_body = body[v_start:v_end].strip()
            v_id = slugify_variant(label)
            v = build_variant(
                section_id=section_id,
                variant_id=v_id,
                section_title=title,
                variant_label=label,
                body=v_body,
            )
            if v:
                variants.append(v)

    return variants


def build_variant(
    section_id: str,
    variant_id: str,
    section_title: str,
    variant_label: str,
    body: str,
) -> Optional[BannerVariant]:
    mascot_match = MASCOT_RE.search(body)
    bg_match = BACKGROUND_RE.search(body)
    if not mascot_match or not bg_match:
        return None
    return BannerVariant(
        section_id=section_id,
        variant_id=variant_id,
        section_title=section_title,
        variant_label=variant_label,
        mascot_prompt=mascot_match.group(1).strip(),
        background_prompt=bg_match.group(1).strip(),
    )


# ---------------------------------------------------------------------------
# Prompt building (UA description + EN tech directives)
# ---------------------------------------------------------------------------

BG_TECH_SUFFIX = (
    "\n\n--- TECH ---\n"
    "Cinematic 3D background, photorealistic-stylized hybrid, depth of field with bokeh, "
    "soft volumetric lighting. Horizontal landscape composition. Main visual focus in the right third "
    "(empty space for a mascot to be added later). Left third should be atmospheric, blurred, slightly darker — "
    "negative space for text overlay. NO TEXT, NO LETTERS, NO LOGOS, NO NUMBERS, NO BUTTONS, NO PEOPLE. "
    "No mascot, no character. Pure background only."
)

MASCOT_TECH_SUFFIX = (
    "\n\n--- TECH ---\n"
    "Same character as in the reference image (blue jelly-like mascot with white headband, "
    "two small antennae/ears on top, big round eyes, wide friendly mouth). Keep the character's body shape, "
    "color, proportions and face fully consistent with the reference. "
    "3D rendered, soft cartoon Pixar style, glossy plastic-like surface, vibrant saturated colors, "
    "cinematic studio lighting, soft rim light, subtle ground shadow. "
    "Full body, 3/4 view. Fully transparent background (alpha channel), no environment, no scenery, "
    "no props except those explicitly described."
)


def build_bg_prompt(v: BannerVariant) -> str:
    header = f"Banner background for: {v.section_title}"
    if v.variant_label:
        header += f" — variant: {v.variant_label}"
    return f"{header}\n\n{v.background_prompt}{BG_TECH_SUFFIX}"


def build_mascot_prompt(v: BannerVariant) -> str:
    header = f"Mascot for: {v.section_title}"
    if v.variant_label:
        header += f" — variant: {v.variant_label}"
    return f"{header}\n\n{v.mascot_prompt}{MASCOT_TECH_SUFFIX}"


# ---------------------------------------------------------------------------
# OpenAI client
# ---------------------------------------------------------------------------

def load_env() -> None:
    if not ENV_FILE.exists():
        return
    for raw in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


def get_client():
    try:
        from openai import OpenAI
    except ImportError as e:
        raise SystemExit(
            "openai package is not installed. Run:\n"
            "  c:/Projects/REPORTS/.venv/Scripts/python.exe -m pip install openai"
        ) from e
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is missing (.env not loaded?).")
    return OpenAI(api_key=api_key)


def save_image_b64(b64: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(base64.b64decode(b64))


def generate_background(client, prompt: str, dest: Path, quality: str) -> None:
    if dest.exists():
        print(f"[skip-bg ] {dest.relative_to(REPO_ROOT)} (already exists)")
        return
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size=BG_SIZE,
        quality=quality,
        n=1,
    )
    save_image_b64(resp.data[0].b64_json, dest)
    print(f"[ok bg   ] {dest.relative_to(REPO_ROOT)}")


def generate_mascot(client, prompt: str, dest: Path, quality: str) -> None:
    if dest.exists():
        print(f"[skip-msc] {dest.relative_to(REPO_ROOT)} (already exists)")
        return
    if not MASCOT_REFERENCE.exists():
        raise SystemExit(f"Mascot reference not found: {MASCOT_REFERENCE}")
    with open(MASCOT_REFERENCE, "rb") as f:
        resp = client.images.edit(
            model="gpt-image-1",
            image=f,
            prompt=prompt,
            size=MASCOT_SIZE,
            quality=quality,
            background="transparent",
            n=1,
        )
    save_image_b64(resp.data[0].b64_json, dest)
    print(f"[ok msc  ] {dest.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quality", choices=["low", "medium", "high"], default="medium")
    ap.add_argument("--only", default="", help="Comma-separated folder names to include")
    ap.add_argument("--skip-bg", action="store_true")
    ap.add_argument("--skip-mascot", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    load_env()

    text = DESCRIPTIONS_FILE.read_text(encoding="utf-8")
    variants = parse_descriptions(text)

    only_filter = {s.strip() for s in args.only.split(",") if s.strip()}
    if only_filter:
        variants = [v for v in variants if v.folder_name in only_filter]

    print(f"Parsed {len(variants)} variants from {DESCRIPTIONS_FILE.name}\n")
    for v in variants:
        marker = "  (cross-ref -> " + CROSS_REFERENCES[v.folder_name] + ")" if v.folder_name in CROSS_REFERENCES else ""
        print(f"  - {v.folder_name:<28} {v.section_title}{marker}")

    if args.dry_run:
        print("\n--- DRY RUN: example prompts for first variant ---")
        if variants:
            v = variants[0]
            print("\n[BG PROMPT]\n" + build_bg_prompt(v))
            print("\n[MASCOT PROMPT]\n" + build_mascot_prompt(v))
        return 0

    client = get_client()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    jobs: list[tuple[str, BannerVariant]] = []
    for v in variants:
        if v.folder_name in CROSS_REFERENCES:
            continue  # handle after main generation
        if not args.skip_bg:
            jobs.append(("bg", v))
        if not args.skip_mascot:
            jobs.append(("mascot", v))

    print(f"\nDispatching {len(jobs)} generation jobs (quality={args.quality}, workers={MAX_WORKERS})...\n")

    started = time.time()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = []
        for kind, v in jobs:
            folder = OUTPUT_DIR / v.folder_name
            if kind == "bg":
                futures.append(
                    ex.submit(
                        generate_background,
                        client,
                        build_bg_prompt(v),
                        folder / "background.png",
                        args.quality,
                    )
                )
            else:
                futures.append(
                    ex.submit(
                        generate_mascot,
                        client,
                        build_mascot_prompt(v),
                        folder / "mascot.png",
                        args.quality,
                    )
                )
        errors = 0
        for fut in as_completed(futures):
            try:
                fut.result()
            except Exception as e:
                errors += 1
                print(f"[ERROR  ] {e}")

    # Resolve cross-references by copying existing outputs.
    import shutil
    for src_folder_name, ref_folder_name in CROSS_REFERENCES.items():
        if only_filter and src_folder_name not in only_filter:
            continue
        src = OUTPUT_DIR / src_folder_name
        ref = OUTPUT_DIR / ref_folder_name
        if not ref.exists():
            print(f"[xref miss] {src_folder_name} -> {ref_folder_name} (source missing)")
            continue
        src.mkdir(parents=True, exist_ok=True)
        for fname in ("background.png", "mascot.png"):
            ref_file = ref / fname
            if ref_file.exists():
                dst = src / fname
                if not dst.exists():
                    shutil.copy2(ref_file, dst)
                    print(f"[xref copy] {dst.relative_to(REPO_ROOT)}")

    elapsed = time.time() - started
    print(f"\nDone in {elapsed:.1f}s. Errors: {errors}.")
    print(f"Output: {OUTPUT_DIR}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
