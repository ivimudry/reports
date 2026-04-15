#!/usr/bin/env python3
"""
DEP Retention — translate hu-HU and pl-PL locales.
Replaces: subject, preheader, text_1, text_2, text_3, button_text_1, default name in personalization.
Preserves: all HTML structure, CSS, promocodes, game names, brand names, URLs.
Winner emails (3C,3S,6C,8S) — text_3 is team sig (already translated), skip it.
"""
import re, os

FILE = r'c:\Projects\REPORTS\тексти\Celsius\DEP Retention - Table data.txt'

text = open(FILE, 'r', encoding='utf-8').read()

# ============================================================
# TRANSLATIONS: (email_name, locale) -> {field: new_value}
# For text_1/text_2/text_3 we replace only the inner text content
# inside the HTML wrapper, so we do targeted string replacements.
# ============================================================

# Helper: builds replacement pairs (old_str, new_str) for each email block
replacements = []

def r(old, new):
    """Register a replacement pair."""
    replacements.append((old, new))

# ===================== Email 1C =====================

# --- hu-HU ---
r('name: Email 1C\nlocale: hu-HU\nsubject: 💥 170% Bonus: Power Up Your Play Today\npreheader: Look what\'s inside to help you win at the tables',
  'name: Email 1C\nlocale: hu-HU\nsubject: 💥 170% Bonus: Turbozd fel a jatekodat ma\npreheader: Nezd meg, mi var rad az asztaloknal')

# text_1: greeting
r('name: Email 1C\nlocale: hu-HU\nsubject: 💥 170% Bonus: Turbozd fel a jatekodat ma\npreheader: Nezd meg, mi var rad az asztaloknal',
  'name: Email 1C\nlocale: hu-HU\nsubject: 💥 170% Bonus: Turbózd fel a játékodat ma\npreheader: Nézd meg, mi vár rád az asztaloknál')

print("NOTE: Using direct file line-level replacements instead.")
print("Aborting approach - switching to line-based replacement script.")
