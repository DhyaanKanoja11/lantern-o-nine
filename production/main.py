# Lantern-o-Nine 9-Key Macropad Firmware
# Created by Dhyaan Kanoja (@DhyaanKanoja11) for Hack Club Hackpad
# Running CircuitPython with KMK Firmware on Seeed Studio XIAO RP2040

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

# -----------------------------------------------------------------------------
# 1. 3x3 SWITCH MATRIX PINOUT (Seeed Xiao RP2040)
# -----------------------------------------------------------------------------
keyboard.row_pins = (board.D2, board.D3, board.D6)
keyboard.col_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# -----------------------------------------------------------------------------
# 2. MODULES & EXTENSIONS
# -----------------------------------------------------------------------------
# Multi-layer support
keyboard.modules.append(Layers())

# Rotary encoder (EC11)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D1, board.D0, None, False),)
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]
keyboard.modules.append(encoder_handler)

# 0.91" 128x32 I2C OLED display (SSD1306)
oled_ext = Oled(
    OledDisplayMode.LAYER,
    oWidth=128,
    oHeight=32,
    reaction_type=OledReactionType.STATIC,
)
keyboard.extensions.append(oled_ext)

# RGB underglow (2x SK6812MINI-E on D10)
rgb = RGB(pixel_pin=board.D10, num_pixels=2)
keyboard.extensions.append(rgb)

# -----------------------------------------------------------------------------
# 3. 3-MODE KEYMAP CONFIGURATION
# -----------------------------------------------------------------------------
# Top Row: Mode switchers (Row 1 is identical across all layers)
#   - Key 1: Mode 1 (Spotify / Media)
#   - Key 2: Mode 2 (Git / Terminal)
#   - Key 3: Mode 3 (Code / IDE)

MODE_SPOTIFY = KC.TO(0)
MODE_GIT     = KC.TO(1)
MODE_CODE    = KC.TO(2)

keyboard.keymap = [
    # Layer 0: Spotify / Media Mode
    [
        MODE_SPOTIFY,   MODE_GIT,        MODE_CODE,
        KC.MPRV,        KC.MPLY,         KC.MNXT,
        KC.VOLD,        KC.MUTE,         KC.VOLU,
    ],
    # Layer 1: Git & Terminal Mode
    [
        MODE_SPOTIFY,   MODE_GIT,        MODE_CODE,
        simple_key_sequence((send_string("git status\n"),)),
        simple_key_sequence((send_string("git add .\n"),)),
        simple_key_sequence((send_string("git commit -m 'update'\n"),)),
        simple_key_sequence((send_string("git push\n"),)),
        KC.LCTL(KC.GRAVE),  # Toggle VS Code terminal
        KC.LCTL(KC.L),      # Clear screen
    ],
    # Layer 2: Code & Editing Mode
    [
        MODE_SPOTIFY,   MODE_GIT,        MODE_CODE,
        KC.LCTL(KC.C),  KC.LCTL(KC.V),   KC.LCTL(KC.X),
        KC.LCTL(KC.Z),  KC.LCTL(KC.Y),   KC.LSFT(KC.LALT(KC.F)),  # Format doc
    ],
]

if __name__ == '__main__':
    keyboard.go()
