#!/usr/bin/env python3
"""
Automation script to render terminal execution figures for Laboratory Work No. 3.
Renders high-resolution terminal captures with Catppuccin Mocha theme.
"""

import os
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/TTF/MesloLGMNerdFontMono-Regular.ttf"
FONT_SIZE = 15
LINE_HEIGHT = 23
PADDING_X = 24
PADDING_Y = 16
HEADER_HEIGHT = 38

# Color Palette (Catppuccin Mocha)
BG_COLOR = (30, 30, 46, 255)         # Base
HEADER_BG = (24, 24, 37, 255)        # Mantle
TEXT_MAIN = (205, 214, 244)         # Text
TEXT_PROMPT = (166, 227, 161)       # Green
TEXT_CMD = (137, 220, 235)          # Cyan
TEXT_INPUT = (249, 226, 175)        # Yellow
TEXT_LABEL = (180, 190, 254)        # Lavender
TEXT_RESULT = (166, 227, 161)       # Green
TEXT_ERROR = (243, 139, 168)        # Red
TEXT_GRID = (147, 153, 178)         # Overlay0
TEXT_GRID_BORDER = (108, 112, 134)  # Surface2
TITLE_COLOR = (166, 173, 200, 255)  # Subtext0


def render_terminal(title: str, lines: list, output_path: str):
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Compute required width
    max_len = 0
    for line_parts in lines:
        total_len = sum(len(part[0]) for part in line_parts)
        if total_len > max_len:
            max_len = total_len

    char_width = 9.2
    width = max(int(max_len * char_width) + PADDING_X * 2, 720)
    height = HEADER_HEIGHT + PADDING_Y * 2 + len(lines) * LINE_HEIGHT

    img = Image.new("RGBA", (width, height), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Window header background
    draw.rectangle([(0, 0), (width, HEADER_HEIGHT)], fill=HEADER_BG)

    # Window control buttons
    draw.ellipse([(14, 13), (26, 25)], fill=(243, 139, 168, 255))  # Red
    draw.ellipse([(34, 13), (46, 25)], fill=(249, 226, 175, 255))  # Yellow
    draw.ellipse([(54, 13), (66, 25)], fill=(166, 227, 161, 255))  # Green

    # Window title centered
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_w) // 2, 10), title, fill=TITLE_COLOR, font=font)

    # Render lines
    y = HEADER_HEIGHT + PADDING_Y
    for line_parts in lines:
        x = PADDING_X
        for text, color in line_parts:
            draw.text((x, y), text, fill=color, font=font)
            bbox = draw.textbbox((x, y), text, font=font)
            x += (bbox[2] - bbox[0])
        y += LINE_HEIGHT

    # Save output PNG
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")


def main():
    img_dir = "report/images"
    os.makedirs(img_dir, exist_ok=True)

    # -----------------------------------------------------------------------
    # 1. Romanian Encryption with Diacritics
    # -----------------------------------------------------------------------
    lines_enc_ro = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("1", TEXT_INPUT)],
        [("Enter the text: ", TEXT_MAIN), ("cifruri polialfabetice și securitatea datelor", TEXT_INPUT)],
        [("Enter the keyword (min 7 chars): ", TEXT_MAIN), ("universitate", TEXT_INPUT)],
        [("Playfair Matrix (6x5):", TEXT_LABEL)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  U |  N |  I |  V |  E |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  R |  S |  T |  A |  Ă |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Â |  B |  C |  D |  F |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  G |  H |  Î |  K |  L |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  M |  O |  P |  Q |  Ș |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Ț |  W |  X |  Y |  Z |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("Plaintext Digraphs : ", TEXT_LABEL), ("CI FR UR IP OL IA LF AB ET IC EȘ IS EC UR IT AT EA DA TE LO RX", TEXT_MAIN)],
        [("Cipher Digraphs    : ", TEXT_LABEL), ("ÎT ÂĂ RÂ TX ȘH VT ȘL SD IĂ TÎ ĂZ NT IF RÂ TC ĂA VĂ KD ĂI HȘ TȚ", TEXT_INPUT)],
        [("Encrypted text     : ", TEXT_LABEL), ("ÎTÂĂRÂTXȘHVTȘLSDIĂTÎĂZNTIFRÂTCĂAVĂKDĂIHȘTȚ", TEXT_RESULT)],
    ]
    render_terminal("playfair.py — Romanian Playfair Encryption", lines_enc_ro, f"{img_dir}/playfair_encrypt_ro.png")

    # -----------------------------------------------------------------------
    # 2. Romanian Decryption
    # -----------------------------------------------------------------------
    lines_dec_ro = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("2", TEXT_INPUT)],
        [("Enter the text: ", TEXT_MAIN), ("ÎTÂĂRÂTXȘHVTȘLSDIĂTÎĂZNTIFRÂTCĂAVĂKDĂIHȘTȚ", TEXT_INPUT)],
        [("Enter the keyword (min 7 chars): ", TEXT_MAIN), ("universitate", TEXT_INPUT)],
        [("Playfair Matrix (6x5):", TEXT_LABEL)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  U |  N |  I |  V |  E |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  R |  S |  T |  A |  Ă |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Â |  B |  C |  D |  F |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  G |  H |  Î |  K |  L |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  M |  O |  P |  Q |  Ș |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Ț |  W |  X |  Y |  Z |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("Cipher Digraphs    : ", TEXT_LABEL), ("ÎT ÂĂ RÂ TX ȘH VT ȘL SD IĂ TÎ ĂZ NT IF RÂ TC ĂA VĂ KD ĂI HȘ TȚ", TEXT_MAIN)],
        [("Decrypted Digraphs : ", TEXT_LABEL), ("CI FR UR IP OL IA LF AB ET IC EȘ IS EC UR IT AT EA DA TE LO RX", TEXT_INPUT)],
        [("Decrypted text     : ", TEXT_LABEL), ("CIFRURIPOLIALFABETICEȘISECURITATEADATELORX", TEXT_RESULT)],
    ]
    render_terminal("playfair.py — Romanian Playfair Decryption", lines_dec_ro, f"{img_dir}/playfair_decrypt_ro.png")

    # -----------------------------------------------------------------------
    # 3. Standard ASCII / General Encryption
    # -----------------------------------------------------------------------
    lines_enc_en = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("1", TEXT_INPUT)],
        [("Enter the text: ", TEXT_MAIN), ("securitatea informatiei", TEXT_INPUT)],
        [("Enter the keyword (min 7 chars): ", TEXT_MAIN), ("criptografie", TEXT_INPUT)],
        [("Playfair Matrix (6x5):", TEXT_LABEL)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  C |  R |  I |  P |  T |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  O |  G |  A |  F |  E |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Ă |  Â |  B |  D |  H |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Î |  K |  L |  M |  N |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Q |  S |  Ș |  Ț |  U |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  V |  W |  X |  Y |  Z |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("Plaintext Digraphs : ", TEXT_LABEL), ("SE CU RI TA TE AI NF OR MA TI EI", TEXT_MAIN)],
        [("Cipher Digraphs    : ", TEXT_LABEL), ("UG TQ IP IE EH BA ME GC LF CP AT", TEXT_INPUT)],
        [("Encrypted text     : ", TEXT_LABEL), ("UGTQIPIEEHBAMEGCLFCPAT", TEXT_RESULT)],
    ]
    render_terminal("playfair.py — Encryption Example", lines_enc_en, f"{img_dir}/playfair_encrypt_en.png")

    # -----------------------------------------------------------------------
    # 4. Standard Decryption
    # -----------------------------------------------------------------------
    lines_dec_en = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("2", TEXT_INPUT)],
        [("Enter the text: ", TEXT_MAIN), ("UGTQIPIEEHBAMEGCLFCPAT", TEXT_INPUT)],
        [("Enter the keyword (min 7 chars): ", TEXT_MAIN), ("criptografie", TEXT_INPUT)],
        [("Playfair Matrix (6x5):", TEXT_LABEL)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  C |  R |  I |  P |  T |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  O |  G |  A |  F |  E |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Ă |  Â |  B |  D |  H |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Î |  K |  L |  M |  N |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  Q |  S |  Ș |  Ț |  U |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("  |  V |  W |  X |  Y |  Z |", TEXT_GRID)],
        [("  +----+----+----+----+----+", TEXT_GRID_BORDER)],
        [("Cipher Digraphs    : ", TEXT_LABEL), ("UG TQ IP IE EH BA ME GC LF CP AT", TEXT_MAIN)],
        [("Decrypted Digraphs : ", TEXT_LABEL), ("SE CU RI TA TE AI NF OR MA TI EI", TEXT_INPUT)],
        [("Decrypted text     : ", TEXT_LABEL), ("SECURITATEAINFORMATIEI", TEXT_RESULT)],
    ]
    render_terminal("playfair.py — Decryption Example", lines_dec_en, f"{img_dir}/playfair_decrypt_en.png")

    # -----------------------------------------------------------------------
    # 5. Input Validation: Keyword Too Short
    # -----------------------------------------------------------------------
    lines_val_key = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("1", TEXT_INPUT)],
        [("Enter the text: ", TEXT_MAIN), ("comunicare secreta", TEXT_INPUT)],
        [("Enter the keyword (min 7 chars): ", TEXT_MAIN), ("cheie", TEXT_INPUT)],
        [("Error: Keyword is too short (5 chars)! It must be at least 7 characters long.", TEXT_ERROR)],
    ]
    render_terminal("playfair.py — Validation: Keyword Too Short", lines_val_key, f"{img_dir}/playfair_invalid_key_short.png")

    # -----------------------------------------------------------------------
    # 6. Input Validation: Invalid Characters & Allowed Range Suggestion
    # -----------------------------------------------------------------------
    lines_val_char = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("1", TEXT_INPUT)],
        [("Enter the text: ", TEXT_MAIN), ("parola_secreta#2026!", TEXT_INPUT)],
        [("Error: Invalid character '_' detected!", TEXT_ERROR)],
        [("Allowed characters: letters from Romanian alphabet (A-Z, a-z, ă, â, î, ș, ț) and spaces.", (249, 226, 175))],
    ]
    render_terminal("playfair.py — Validation: Invalid Character Range", lines_val_char, f"{img_dir}/playfair_invalid_char.png")

    # -----------------------------------------------------------------------
    # 7. Input Validation: Invalid Operation Choice
    # -----------------------------------------------------------------------
    lines_val_op = [
        [("ilie@archlinux:~/CS/lab3$ ", TEXT_PROMPT), ("python3 playfair.py", TEXT_CMD)],
        [("Playfair Cipher", TEXT_LABEL)],
        [("Choose the operation:", TEXT_MAIN)],
        [("1. Encrypt", TEXT_MAIN)],
        [("2. Decrypt", TEXT_MAIN)],
        [("Operation (1/2): ", TEXT_MAIN), ("5", TEXT_INPUT)],
        [("Error: Invalid operation choice! Please select 1 or 2.", TEXT_ERROR)],
    ]
    render_terminal("playfair.py — Validation: Invalid Operation", lines_val_op, f"{img_dir}/playfair_invalid_op.png")


if __name__ == "__main__":
    main()
