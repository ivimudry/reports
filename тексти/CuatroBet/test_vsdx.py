"""
Generate Visio .vsdx for CuatroBet 01-Day1 Retention Layer.
Uses vsdx library with built-in template for valid OOXML output.
Oshi Miro style: semi-transparent fills, dark strokes, arrows.
Full detail on both Slots and Aviator paths.
"""
import vsdx
import copy
import os
import xml.etree.ElementTree as ET

OUT_DIR = r"c:\Projects\REPORTS\тексти\CuatroBet\implementation-guide-visio"
os.makedirs(OUT_DIR, exist_ok=True)
TEMPLATE = r"C:\Projects\REPORTS\.venv\Lib\site-packages\vsdx\media\media.vsdx"

NS = '{http://schemas.microsoft.com/office/visio/2012/main}'

# ── Oshi-style colors ─────────────────────────────────
# In Visio: FillForegndTrans = 0..1 (0=opaque, 1=transparent)
STYLES = {
    'trigger':  {'fill': '#2dc75c', 'trans': 0.3},   # green, 70% opacity
    'action':   {'fill': '#659df2', 'trans': 0.6},    # blue, 40% opacity
    'decision': {'fill': '#dedaff', 'trans': 0.6},    # purple, 40% opacity
    'email':    {'fill': '#659df2', 'trans': 0.6},    # blue, 40% opacity
    'sms':      {'fill': '#fffd00', 'trans': 0.3},    # yellow, 70% opacity
    'popup':    {'fill': '#ffc6c6', 'trans': 0.6},    # pink, 40% opacity
    'widget':   {'fill': '#ffc6c6', 'trans': 0.6},    # pink, 40% opacity
    'wait':     {'fill': '#fff6b6', 'trans': 0.0},    # yellow, 100% opacity
    'exit':     {'fill': '#ffc6c6', 'trans': 0.6},    # pink, 40% opacity
    'branch':   {'fill': '#dedaff', 'trans': 0.6},    # purple, 40% opacity
}

# ── Flow definition ───────────────────────────────────
PAGE_W = 16.0
SLOT_X = 3.0
AVI_X = 11.0
SHARED_X = 7.0
Y_STEP = 1.6

nodes = []
connectors = []

def add_node(ntype, label, x, y, w=3.0, h=0.85):
    nid = len(nodes) + 1
    nodes.append({
        'id': nid, 'type': ntype, 'label': label,
        'x': x, 'y': y, 'w': w, 'h': h,
    })
    return nid

def add_conn(from_id, to_id, label=''):
    connectors.append({'from': from_id, 'to': to_id, 'label': label})


# ═══════════════════════════════════════════════════════
#   BUILD COMPLETE FLOW
# ═══════════════════════════════════════════════════════

y = 1.0
n_entry = add_node('trigger', 'FTD Event\ndeposit_success (is_ftd=true)', SHARED_X, y, 3.5, 0.9)

y += Y_STEP
n_branch = add_node('branch', 'Branch: game_preference\nSlots vs Aviator', SHARED_X, y, 3.2, 0.85)
add_conn(n_entry, n_branch)

# ═══════ SLOTS PATH (LEFT) ═══════════════════════════
y_s = y + Y_STEP
n_s_t1 = add_node('action', 'T1: Bonus Grant\n50 FS Gates of Olympus\nWBL-S-D1, 20x, 24h', SLOT_X, y_s, 3.2, 0.95)
add_conn(n_branch, n_s_t1, 'Slots (95%)')

y_s += Y_STEP
n_s_t2 = add_node('popup', 'T2: Welcome Popup (+5min)\nBienvenido a CuatroBet!\nBono 120% + 50 giros gratis', SLOT_X, y_s, 3.2, 0.95)
add_conn(n_s_t1, n_s_t2)

y_s += Y_STEP
n_s_d1 = add_node('decision', 'T+30min\nStill in session?', SLOT_X, y_s, 2.8, 0.8)
add_conn(n_s_t2, n_s_d1)

y_s += Y_STEP
n_s_t3 = add_node('widget', 'T3: AI Game Reco (+1h)\n3 similar slots\nGR8 Tech AI module', SLOT_X - 2.0, y_s, 3.0, 0.95)
add_conn(n_s_d1, n_s_t3, 'YES')

n_s_t4 = add_node('sms', 'T4: Session Exit SMS (+2h)\nTus 50 giros gratis en\nGates of Olympus vencen en 22h', SLOT_X + 2.0, y_s, 3.2, 0.95)
add_conn(n_s_d1, n_s_t4, 'NO')

y_s += Y_STEP
n_s_d2 = add_node('decision', 'T+6h\nPlayer returned?', SLOT_X, y_s, 2.8, 0.8)
add_conn(n_s_t3, n_s_d2)
add_conn(n_s_t4, n_s_d2)

y_s += Y_STEP
n_s_t5a = add_node('popup', 'T5A: Reward Popup\nGracias por volver!\n100 CC gratis', SLOT_X - 2.0, y_s, 3.0, 0.95)
add_conn(n_s_d2, n_s_t5a, 'YES')

n_s_t5b = add_node('sms', 'T5B: Urgency SMS\n1,000 ARS extra\nsi depositas en 6 horas', SLOT_X + 2.0, y_s, 3.0, 0.95)
add_conn(n_s_d2, n_s_t5b, 'NO')

y_s += Y_STEP
n_s_d3 = add_node('decision', 'T+24h\nReturned in 24h?', SLOT_X, y_s, 2.8, 0.8)
add_conn(n_s_t5a, n_s_d3)
add_conn(n_s_t5b, n_s_d3)

y_s += Y_STEP
n_s_exit1 = add_node('exit', 'EXIT\nPost-FTD Lifecycle', SLOT_X - 2.0, y_s, 2.5, 0.75)
add_conn(n_s_d3, n_s_exit1, 'YES')

n_s_t6 = add_node('email', 'T6: Email Reload (24h)\n75% + 20 giros gratis\nJokers Jewels, 25x, 48h', SLOT_X + 2.0, y_s, 3.2, 0.95)
add_conn(n_s_d3, n_s_t6, 'NO')

y_s += Y_STEP
n_s_d4 = add_node('decision', 'T+48h\nStill inactive?', SLOT_X + 2.0, y_s, 2.8, 0.8)
add_conn(n_s_t6, n_s_d4)

y_s += Y_STEP
n_s_exit2 = add_node('exit', 'EXIT\nPost-FTD Lifecycle', SLOT_X + 0.5, y_s, 2.5, 0.75)
add_conn(n_s_d4, n_s_exit2, 'NO')

n_s_t7 = add_node('sms', 'T7: Final SMS (48h)\n500 ARS free bet Aviator\n1x wagering, 24h', SLOT_X + 3.5, y_s, 3.0, 0.95)
add_conn(n_s_d4, n_s_t7, 'YES')

y_s += Y_STEP
n_s_d5 = add_node('decision', 'T+72h\nFinal check', SLOT_X + 3.5, y_s, 2.5, 0.8)
add_conn(n_s_t7, n_s_d5)

y_s += Y_STEP
n_s_exit3 = add_node('exit', 'EXIT\nPost-FTD Lifecycle', SLOT_X + 2.0, y_s, 2.5, 0.75)
add_conn(n_s_d5, n_s_exit3, 'Returned')

n_s_exit4 = add_node('exit', 'EXIT\nReactivation Ladder\n(Early Churn Day 3)', SLOT_X + 5.0, y_s, 2.8, 0.85)
add_conn(n_s_d5, n_s_exit4, 'Never returned')


# ═══════ AVIATOR PATH (RIGHT) ════════════════════════
y_a = y + Y_STEP
n_a_t1 = add_node('action', 'T1: Bonus Grant\n5 Free Flights Aviator\n24h expiry', AVI_X, y_a, 3.2, 0.95)
add_conn(n_branch, n_a_t1, 'Aviator (5%)')

y_a += Y_STEP
n_a_t2 = add_node('popup', 'T2: Welcome Popup (+5min)\nBienvenido a CuatroBet!\n5 Free Flights en Aviator listos', AVI_X, y_a, 3.2, 0.95)
add_conn(n_a_t1, n_a_t2)

y_a += Y_STEP
n_a_d1 = add_node('decision', 'T+30min\nStill in session?', AVI_X, y_a, 2.8, 0.8)
add_conn(n_a_t2, n_a_d1)

y_a += Y_STEP
n_a_t3 = add_node('widget', 'T3: AI Game Reco (+1h)\n3 crash/instant games\nGR8 Tech AI module', AVI_X - 2.0, y_a, 3.0, 0.95)
add_conn(n_a_d1, n_a_t3, 'YES')

n_a_t4 = add_node('sms', 'T4: Session Exit SMS (+2h)\nTus Free Flights en\nAviator vencen en 22h', AVI_X + 2.0, y_a, 3.2, 0.95)
add_conn(n_a_d1, n_a_t4, 'NO')

y_a += Y_STEP
n_a_d2 = add_node('decision', 'T+6h\nPlayer returned?', AVI_X, y_a, 2.8, 0.8)
add_conn(n_a_t3, n_a_d2)
add_conn(n_a_t4, n_a_d2)

y_a += Y_STEP
n_a_t5a = add_node('popup', 'T5A: Reward Popup\nGracias por volver!\n100 CC gratis', AVI_X - 2.0, y_a, 3.0, 0.95)
add_conn(n_a_d2, n_a_t5a, 'YES')

n_a_t5b = add_node('sms', 'T5B: Urgency SMS\n1,000 ARS extra\nsi depositas en 6 horas', AVI_X + 2.0, y_a, 3.0, 0.95)
add_conn(n_a_d2, n_a_t5b, 'NO')

y_a += Y_STEP
n_a_d3 = add_node('decision', 'T+24h\nReturned in 24h?', AVI_X, y_a, 2.8, 0.8)
add_conn(n_a_t5a, n_a_d3)
add_conn(n_a_t5b, n_a_d3)

y_a += Y_STEP
n_a_exit1 = add_node('exit', 'EXIT\nPost-FTD Lifecycle', AVI_X - 2.0, y_a, 2.5, 0.75)
add_conn(n_a_d3, n_a_exit1, 'YES')

n_a_t6 = add_node('email', 'T6: Email Reload (24h)\n75% + 10 Free Flights\nAviator, 15x wagering', AVI_X + 2.0, y_a, 3.2, 0.95)
add_conn(n_a_d3, n_a_t6, 'NO')

y_a += Y_STEP
n_a_d4 = add_node('decision', 'T+48h\nStill inactive?', AVI_X + 2.0, y_a, 2.8, 0.8)
add_conn(n_a_t6, n_a_d4)

y_a += Y_STEP
n_a_exit2 = add_node('exit', 'EXIT\nPost-FTD Lifecycle', AVI_X + 0.5, y_a, 2.5, 0.75)
add_conn(n_a_d4, n_a_exit2, 'NO')

n_a_t7 = add_node('sms', 'T7: Final SMS (48h)\n500 ARS free bet Aviator\n1x wagering, 24h', AVI_X + 3.5, y_a, 3.0, 0.95)
add_conn(n_a_d4, n_a_t7, 'YES')

y_a += Y_STEP
n_a_d5 = add_node('decision', 'T+72h\nFinal check', AVI_X + 3.5, y_a, 2.5, 0.8)
add_conn(n_a_t7, n_a_d5)

y_a += Y_STEP
n_a_exit3 = add_node('exit', 'EXIT\nPost-FTD Lifecycle', AVI_X + 2.0, y_a, 2.5, 0.75)
add_conn(n_a_d5, n_a_exit3, 'Returned')

n_a_exit4 = add_node('exit', 'EXIT\nReactivation Ladder\n(Early Churn Day 3)', AVI_X + 5.0, y_a, 2.8, 0.85)
add_conn(n_a_d5, n_a_exit4, 'Never returned')

# Adjust page height
PAGE_H = max(y_s, y_a) + 3.0


def vy(ytop):
    """Convert top-down Y to Visio bottom-up Y."""
    return PAGE_H - ytop


# ═══════════════════════════════════════════════════════
#   BUILD VSDX using library
# ═══════════════════════════════════════════════════════

def set_cell(shape, name, value):
    """Set or create a Cell element on a shape."""
    for cell in shape.xml.findall(NS + 'Cell'):
        if cell.get('N') == name:
            cell.set('V', str(value))
            if 'F' in cell.attrib:
                del cell.attrib['F']
            return
    cell = ET.SubElement(shape.xml, NS + 'Cell')
    cell.set('N', name)
    cell.set('V', str(value))


with vsdx.VisioFile(TEMPLATE) as vis:
    page = vis.pages[0]
    page.name = 'Day 1 Retention Layer'

    # Get template shapes before clearing
    rect_template = page.find_shape_by_id('1')
    conn_template = page.find_shape_by_id('3')

    # Remove all existing template shapes (except those we need as templates)
    shapes_to_remove = [s for s in page.child_shapes if s.ID not in ('1', '3')]
    for shape in shapes_to_remove:
        shape.remove()

    shape_map = {}

    # ── Create box shapes ─────────────────────────────
    for n in nodes:
        new_shape = rect_template.copy(page)

        style = STYLES.get(n['type'], STYLES['action'])
        cx = n['x'] + n['w'] / 2
        cy = vy(n['y']) - n['h'] / 2

        set_cell(new_shape, 'PinX', cx)
        set_cell(new_shape, 'PinY', cy)
        set_cell(new_shape, 'Width', n['w'])
        set_cell(new_shape, 'Height', n['h'])
        set_cell(new_shape, 'LocPinX', n['w'] / 2)
        set_cell(new_shape, 'LocPinY', n['h'] / 2)

        # Fill
        set_cell(new_shape, 'FillForegnd', style['fill'])
        set_cell(new_shape, 'FillBkgnd', style['fill'])
        set_cell(new_shape, 'FillForegndTrans', style['trans'])
        set_cell(new_shape, 'FillBkgndTrans', style['trans'])

        # Line
        set_cell(new_shape, 'LineColor', '#1a1a1a')
        set_cell(new_shape, 'LineWeight', '0.02777')
        set_cell(new_shape, 'Rounding', '0.1')

        # Text
        new_shape.text = n['label']

        # Character section
        char_sec = ET.SubElement(new_shape.xml, NS + 'Section')
        char_sec.set('N', 'Character')
        char_row = ET.SubElement(char_sec, NS + 'Row')
        char_row.set('IX', '0')
        for cn, cv in [('Font', 'Calibri'), ('Size', '0.1111'), ('Color', '#1a1a1a'), ('Style', '0')]:
            c = ET.SubElement(char_row, NS + 'Cell')
            c.set('N', cn)
            c.set('V', cv)

        # Paragraph center
        para_sec = ET.SubElement(new_shape.xml, NS + 'Section')
        para_sec.set('N', 'Paragraph')
        para_row = ET.SubElement(para_sec, NS + 'Row')
        para_row.set('IX', '0')
        hc = ET.SubElement(para_row, NS + 'Cell')
        hc.set('N', 'HorzAlign')
        hc.set('V', '1')

        set_cell(new_shape, 'VerticalAlign', '1')

        shape_map[n['id']] = new_shape

    # Now remove the original templates
    rect_template.remove()
    conn_template.remove()
    # Also remove any other leftover template shapes
    for s in list(page.child_shapes):
        if s.ID in ('1', '2', '3', '5', '7', '8'):
            try:
                s.remove()
            except Exception:
                pass

    # ── Create connectors ─────────────────────────────
    for c in connectors:
        new_conn = conn_template.copy(page)

        fn = next(n for n in nodes if n['id'] == c['from'])
        tn = next(n for n in nodes if n['id'] == c['to'])

        bx = fn['x'] + fn['w'] / 2
        by = vy(fn['y']) - fn['h']
        ex = tn['x'] + tn['w'] / 2
        ey = vy(tn['y'])

        set_cell(new_conn, 'BeginX', bx)
        set_cell(new_conn, 'BeginY', by)
        set_cell(new_conn, 'EndX', ex)
        set_cell(new_conn, 'EndY', ey)

        w = ex - bx
        h = ey - by
        set_cell(new_conn, 'PinX', bx + w / 2)
        set_cell(new_conn, 'PinY', by + h / 2)
        set_cell(new_conn, 'Width', w)
        set_cell(new_conn, 'Height', h)
        set_cell(new_conn, 'LocPinX', w / 2)
        set_cell(new_conn, 'LocPinY', h / 2)

        set_cell(new_conn, 'LineColor', '#333333')
        set_cell(new_conn, 'LineWeight', '0.01388')
        set_cell(new_conn, 'EndArrow', '13')
        set_cell(new_conn, 'EndArrowSize', '2')
        set_cell(new_conn, 'ShapeRouteStyle', '1')
        set_cell(new_conn, 'ConFixedCode', '6')

        # Update geometry
        for sec in new_conn.xml.findall(NS + 'Section'):
            if sec.get('N') == 'Geometry':
                for row in sec.findall(NS + 'Row'):
                    if row.get('IX') == '2':
                        for cell in row.findall(NS + 'Cell'):
                            if cell.get('N') == 'X':
                                cell.set('V', str(w))
                            if cell.get('N') == 'Y':
                                cell.set('V', str(h))

        # Text label
        new_conn.text = c.get('label', '')

        if c.get('label'):
            set_cell(new_conn, 'TxtPinX', w / 2)
            set_cell(new_conn, 'TxtPinY', h / 2)
            set_cell(new_conn, 'TxtWidth', '0.8')
            set_cell(new_conn, 'TxtHeight', '0.2')
            set_cell(new_conn, 'TxtLocPinX', '0.4')
            set_cell(new_conn, 'TxtLocPinY', '0.1')

            char_sec = ET.SubElement(new_conn.xml, NS + 'Section')
            char_sec.set('N', 'Character')
            char_row = ET.SubElement(char_sec, NS + 'Row')
            char_row.set('IX', '0')
            for cn, cv in [('Font', 'Calibri'), ('Size', '0.0833'), ('Color', '#666666'), ('Style', '1')]:
                ce = ET.SubElement(char_row, NS + 'Cell')
                ce.set('N', cn)
                ce.set('V', cv)

    # Save
    out_path = os.path.join(OUT_DIR, '01-day1-retention-layer.vsdx')
    vis.save_vsdx(out_path)

print('Created: %s' % out_path)
print('Nodes: %d, Connectors: %d' % (len(nodes), len(connectors)))
print('Page: %.0f x %.0f inches' % (PAGE_W, PAGE_H))
