# 🏮 Lantern-o-Nine

> **A 9-Key Custom Mechanical Macropad with Rotary Encoder, OLED Display, and RGB Underglow**  
> Designed and built by **Dhyaan Kanoja** ([@DhyaanKanoja11](https://github.com/DhyaanKanoja11)) for the [Hack Club Hackpad](https://hackpad.hackclub.com/) initiative.

---

## 📸 Gallery & Visuals

### 3D PCB Renders
| 3D Isometric View | Top View | Bottom View |
| :---: | :---: | :---: |
| ![Isometric Render](images/render_iso.png) | ![Top Render](images/render_top.png) | ![Bottom Render](images/render_bottom.png) |

### Schematic & PCB Layout
| Complete Schematic | 2D PCB Layout |
| :---: | :---: |
| ![KiCad Schematic](images/schematic.svg) | ![PCB Layout](images/pcb_layout.svg) |

---

## 💡 Why I Built Lantern-o-Nine

As a student and programmer, I spend hours switching between IDEs, terminal tabs, design tools, and music playlists. I found myself repeatedly typing the same shortcut combinations or reaching across the desk to adjust audio levels. 

When I discovered Hack Club's **Hackpad** program, I saw the perfect opportunity to build my dream desktop companion from the ground up:
1. **Dedicated Productivity Macros:** 9 mechanical switches arranged in a 3×3 grid for rapid editing, code execution, and terminal navigation.
2. **Tactile Media Control:** A smooth EC11 rotary encoder knob with push-to-mute for quick audio control without leaving my code.
3. **Live Visual Telemetry:** A crisp 0.91" OLED display to monitor active layers, volume levels, and status.
4. **Ambient Mood Lighting:** Dual reverse-mount SK6812MINI-E addressable RGB LEDs shining through the PCB cutouts onto the desk.
5. **Personalized 3D Case:** A snap-fit, two-piece enclosure featuring my own custom debossed `"Lantern-o-Nine"` branding and an acoustic honeycomb ventilation rosette.

---

## 🛠️ The Design Journey & Human Engineering

Designing this board in KiCad was an incredible hands-on learning experience:

- **Human-Guided Routing (No AI / No Autotracers):** Rather than relying on black-box automated autorouters or complex net class overrides, I routed the traces by hand using clean, beginner-friendly 0.3mm signal tracks and 0.5mm power rails.
- **Anti-Ghosting 3×3 Matrix:** Each of the 9 Cherry MX switches has its own dedicated 1N4148 switching diode (`ROW2COL`), ensuring complete N-Key Rollover (NKRO) with zero ghosting during fast typing.
- **Solid Power Distribution & Ground Pours:** A full bottom-copper ground plane (`B.Cu`) connected to thermal relief pads and ground stitching vias provides low-noise return paths for the microcontroller, display, and RGB LEDs.
- **3D Case Design:** Designed in CAD with tight tolerances (0.6mm perimeter clearance, 2.0mm switch mounting plate, recessed PCB shelf, and USB-C port cutout). The bottom case includes a subtle 7-hexagon honeycomb grille for ventilation and debossed typography.

---

## 📐 Specifications & Hack Club Compliance

| Parameter | Project Value | Hack Club Requirement | Status |
| :--- | :--- | :--- | :---: |
| **Microcontroller** | Seeed Studio XIAO RP2040 (Through-Hole) | Seeed XIAO RP2040 required | ✅ Compliant |
| **PCB Dimensions** | **96.0 mm × 99.5 mm** | Must be ≤ 100 mm × 100 mm | ✅ Compliant |
| **Layer Count** | **2 Layers** (`F.Cu` & `B.Cu`) | 2 layers maximum | ✅ Compliant |
| **Total Inputs** | **10 Inputs** (9 switches + 1 rotary encoder) | Fewer than 16 inputs | ✅ Compliant |
| **DRC Violations** | **0 Errors, 0 Unconnected Nets** | Must pass DRC | ✅ Compliant |
| **Case Dimensions**| **102.0 mm × 105.5 mm × 15.2 mm** | Must fit in 200 × 200 × 100 mm | ✅ Compliant |
| **Case Construction** | 100% 3D Printable (PLA / PETG) | 3D printed only (no CNC/acrylic)| ✅ Compliant |

---

## 🔌 Pinout Mapping

All components map to the Seeed Studio XIAO RP2040 microcontroller:

| Xiao Pin | RP2040 GPIO | Function | Connected Hardware |
| :--- | :--- | :--- | :--- |
| **D0** | GPIO26 | **Encoder B** | EC11 Rotary Encoder Channel B |
| **D1** | GPIO27 | **Encoder A** | EC11 Rotary Encoder Channel A |
| **D2** | GPIO28 | **Row 1** | Matrix Row 1 (Diodes D1, D2, D3) |
| **D3** | GPIO29 | **Row 2** | Matrix Row 2 (Diodes D4, D5, D6) |
| **D4** | GPIO6  | **I2C SDA** | 0.91" 128×32 OLED Data |
| **D5** | GPIO7  | **I2C SCL** | 0.91" 128×32 OLED Clock |
| **D6** | GPIO0  | **Row 3** | Matrix Row 3 (Diodes D7, D8, D9) |
| **D7** | GPIO1  | **Col 1** | Matrix Column 1 (Switches SW2, SW5, SW8) |
| **D8** | GPIO2  | **Col 2** | Matrix Column 2 (Switches SW3, SW6, SW9) |
| **D9** | GPIO4  | **Col 3** | Matrix Column 3 (Switches SW4, SW7, SW10) |
| **D10** | GPIO3  | **LED DATA**| SK6812MINI-E Addressable RGB DIN |
| **3V3** | 3.3V   | **3.3V Power** | OLED Display VCC |
| **5V**  | 5.0V   | **5.0V Power** | SK6812MINI-E VDD Supply |
| **GND** | GND    | **Ground** | Continuous Ground Planes (`F.Cu` & `B.Cu`) |

---

## 📦 Bill of Materials (BOM)

| Item | Reference | Qty | Package / Footprint | Description & Sourcing |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **U2** | 1 | Through-Hole Module | [Seeed Studio XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) |
| 2 | **SW2–SW10** | 9 | Standard MX Footprint | [Cherry MX / Gateron Mechanical Switches](https://hackpad.hackclub.com) |
| 3 | **D1–D9** | 9 | DO-35 (Through-Hole) | 1N4148 Fast Switching Diodes |
| 4 | **SW1** | 1 | EC11 Through-Hole | [EC11 Rotary Encoder with Push Button](https://hackpad.hackclub.com) |
| 5 | **U1** | 1 | 1×4 Pin Header (2.54mm) | [0.91" 128×32 I2C OLED Display (SSD1306)](https://hackpad.hackclub.com) |
| 6 | **D10, D11** | 2 | 3.2×2.8mm Reverse-Mount | [SK6812MINI-E Addressable RGB LEDs](https://hackpad.hackclub.com) |
| 7 | **C1, C2** | 2 | 0805 SMD | 0.1 µF (100nF) Ceramic Decoupling Capacitors |
| 8 | **Case** | 1 | 3D Printed | Switch Plate (`Top.STEP`) + Base Shell (`Bottom.STEP`) |

---

## 💻 Firmware Setup (CircuitPython + KMK)

The macropad runs open-source **CircuitPython** with **KMK Firmware**, making key remapping as simple as editing a Python script on a USB flash drive!

### 1. Flash CircuitPython
1. Hold down the `BOOT` button on the XIAO RP2040 and connect the USB-C cable to your computer.
2. A drive named `RPI-RP2` will appear.
3. Download the latest CircuitPython UF2 for Seeed XIAO RP2040 from [CircuitPython.org](https://circuitpython.org/board/seeed_xiao_rp2040/) and drag it onto the drive.
4. The board will reboot and mount as `CIRCUITPY`.

### 2. Install KMK
1. Download the [KMK Firmware repository](https://github.com/KMKfw/kmk_firmware).
2. Copy the `kmk/` folder into the root of your `CIRCUITPY` drive.

### 3. Load Macropad Code
Copy [`Firmware/main.py`](Firmware/main.py) to your `CIRCUITPY` drive as `code.py`.

### Default Keymap Configuration

| Key | Action | Function |
| :---: | :---: | :---: |
| **Row 1** | `Esc` \| `Mute Media` \| `Play/Pause` | System Navigation & Media |
| **Row 2** | `Ctrl/Cmd + X` \| `Ctrl/Cmd + C` \| `Ctrl/Cmd + V` | Cut, Copy, Paste Clipboard |
| **Row 3** | `Ctrl/Cmd + Z` \| `Ctrl/Cmd + Y` \| `Enter` | Undo, Redo, Submit |
| **Encoder** | Rotate: `Volume Down / Up` \| Click: `Mute` | Master Volume Knob |

*(You can easily customize these in `Firmware/main.py`!)*

---

## 📁 Repository Structure

```text
lantern-o-nine/
├── README.md                 # Complete project documentation & guide
├── .gitignore                # KiCad and build artifact ignore rules
├── CAD/                      # 3D Mechanical CAD Models
│   ├── assembled-model.STEP  # Full assembly (Bottom + PCB + Top)
│   ├── Top.STEP              # Top switch plate with debossed branding
│   └── Bottom.STEP           # Bottom case with honeycomb vent rosette
├── PCB/                      # KiCad 10 Source Files
│   ├── hackpadtrial.kicad_pro# KiCad Project File
│   ├── hackpadtrial.kicad_sch# Schematic (Title: Lantern-o-Nine Hackpad)
│   ├── hackpadtrial.kicad_pcb# PCB Layout (96.0 x 99.5 mm, 0 DRC errors)
│   └── hackpadtrial.kicad_prl# Project Local Settings
├── Firmware/                 # Open-Source Firmware
│   └── main.py               # CircuitPython & KMK keyboard definition
├── production/               # Ready-to-Manufacture Artifacts
│   ├── gerbers.zip           # 2-Layer Gerber & Drill files for JLCPCB/PCBWay
│   ├── Top.STEP              # Switch plate STEP file
│   ├── Bottom.STEP           # Bottom case STEP file
│   └── main.py               # Production firmware script
└── images/                   # Visual Documentation Assets
    ├── render_iso.png        # 3D raytraced isometric render
    ├── render_top.png        # 3D raytraced top view render
    ├── render_bottom.png     # 3D raytraced bottom view render
    ├── schematic.svg         # Crisp vector schematic diagram
    └── pcb_layout.svg        # Crisp vector 2D PCB routing diagram
```

---

## 🤝 Acknowledgments & License

- Special thanks to the **Hack Club** community and team for organizing the [Hackpad](https://hackpad.hackclub.com/) program.
- Designed with passion by **Dhyaan Kanoja** ([@DhyaanKanoja11](https://github.com/DhyaanKanoja11)).
- Licensed under the **MIT License** — feel free to build, customize, and hack your own!
