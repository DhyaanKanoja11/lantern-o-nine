# Lantern-o-Nine 9-Key Macropad Firmware
# Created by Dhyaan Kanoja (@DhyaanKanoja11) for Hack Club Hackpad
# Running CircuitPython with KMK Firmware on Seeed Studio XIAO RP2040

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType
from kmk.extensions.RGB import RGB

# Initialize keyboard instance
keyboard = KMKKeyboard()

# -----------------------------------------------------------------------------
# 1. 3x3 SWITCH MATRIX PINOUT (Seeed Xiao RP2040)
# -----------------------------------------------------------------------------
# Rows connect to diode cathodes; columns connect to switch inputs.
# Diode orientation is ROW2COL to prevent ghosting when pressing multiple keys.
keyboard.row_pins = (board.D2, board.D3, board.D6)
keyboard.col_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# -----------------------------------------------------------------------------
# 2. ROTARY ENCODER (EC11)
# -----------------------------------------------------------------------------
# Encoder channel A connects to D1, channel B connects to D0.
# Turning clockwise increases volume, counter-clockwise decreases volume.
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D1, board.D0, None, False),
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]

# -----------------------------------------------------------------------------
# 3. 0.91" 128x32 I2C OLED DISPLAY (SSD1306)
# -----------------------------------------------------------------------------
# SDA is on D4, SCL is on D5.
# Displays active layers, lock status, and real-time macropad telemetry.
oled_ext = Oled(
    OledDisplayMode.LAYER,
    oWidth=128,
    oHeight=32,
    reaction_type=OledReactionType.STATIC,
)
keyboard.extensions.append(oled_ext)

# -----------------------------------------------------------------------------
# 4. SK6812MINI-E REVERSE-MOUNT RGB LEDS (Underglow)
# -----------------------------------------------------------------------------
# Data In routes from Xiao pin D10 (Pin 11).
# 2 reverse-mount LEDs illuminate through the PCB cutouts for desk underglow.
rgb = RGB(pixel_pin=board.D10, num_pixels=2)
keyboard.extensions.append(rgb)

# -----------------------------------------------------------------------------
# 5. KEYMAP CONFIGURATION (Customize your shortcuts here!)
# -----------------------------------------------------------------------------
# Layout:
# [ Key 1: Esc       ] [ Key 2: Mute Media ] [ Key 3: Play/Pause ]
# [ Key 4: Cut (X)   ] [ Key 5: Copy (C)   ] [ Key 6: Paste (V)  ]
# [ Key 7: Undo (Z)  ] [ Key 8: Redo (Y)   ] [ Key 9: Enter      ]

keyboard.keymap = [
    [
        KC.ESC,           KC.MUTE,         KC.MPLY,
        KC.LCMD(KC.X),    KC.LCMD(KC.C),   KC.LCMD(KC.V),
        KC.LCMD(KC.Z),    KC.LCMD(KC.Y),   KC.ENTER,
    ]
]

# Start the keyboard loop
if __name__ == '__main__':
    keyboard.go()
