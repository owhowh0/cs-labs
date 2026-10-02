#!/usr/bin/env python3
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/TTF/MesloLGMNerdFontMono-Regular.ttf"
FONT_SIZE = 16
LINE_HEIGHT = 24
PADDING_X = 24
PADDING_Y = 16
HEADER_HEIGHT = 38


def render_terminal(title, lines, output_path):
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    bold_font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Calculate dimensions
    max_len = 0
    for line_parts in lines:
        total_len = sum(len(part[0]) for part in line_parts)
        if total_len > max_len:
            max_len = total_len

    char_width = 9.8
    width = max(int(max_len * char_width) + PADDING_X * 2, 680)
    height = HEADER_HEIGHT + PADDING_Y * 2 + len(lines) * LINE_HEIGHT

    # Create image
    img = Image.new("RGBA", (width, height), (30, 30, 46, 255))
    draw = ImageDraw.Draw(img)

    # Window header background
    draw.rectangle([(0, 0), (width, HEADER_HEIGHT)], fill=(24, 24, 37, 255))

    # Window buttons
    draw.ellipse([(14, 13), (26, 25)], fill=(243, 139, 168, 255))  # Red
    draw.ellipse([(34, 13), (46, 25)], fill=(249, 226, 175, 255))  # Yellow
    draw.ellipse([(54, 13), (66, 25)], fill=(166, 227, 161, 255))  # Green

    # Window title
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_w) // 2, 10), title, fill=(166, 173, 200, 255), font=font)

    # Render lines
    y = HEADER_HEIGHT + PADDING_Y
    for line_parts in lines:
        x = PADDING_X
        for text, color in line_parts:
            draw.text((x, y), text, fill=color, font=font)
            bbox = draw.textbbox((x, y), text, font=font)
            x += (bbox[2] - bbox[0])
        y += LINE_HEIGHT

    # Save image
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")


def main():
    os.makedirs("report/images", exist_ok=True)

    # 1. Caesar 1 Encrypt
    lines1 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar1.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("1", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("securitatea informatiei", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("5", (249, 226, 175))],
        [("Encrypted text: ", (180, 190, 254)), ("vîhzumxdxîd msjșurdxmîm", (166, 227, 161))],
    ]
    render_terminal("caesar1.py — Encryption", lines1, "report/images/caesar1_encrypt.png")

    # 2. Caesar 1 Decrypt
    lines2 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar1.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("2", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("vîhzumxdxîd msjșurdxmîm", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("5", (249, 226, 175))],
        [("Decrypted text: ", (180, 190, 254)), ("securitatea informatiei", (166, 227, 161))],
    ]
    render_terminal("caesar1.py — Decryption", lines2, "report/images/caesar1_decrypt.png")

    # 3. Caesar 1 Invalid Key
    lines3 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar1.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("1", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("laborator criptografie", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("35", (249, 226, 175))],
        [("Error: Invalid key! The numeric key must be an integer between 1 and 30.", (243, 139, 168))],
    ]
    render_terminal("caesar1.py — Invalid Key Validation", lines3, "report/images/caesar1_invalid_key.png")

    # 4. Caesar 1 Invalid Character
    lines4 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar1.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("1", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("parola123!", (249, 226, 175))],
        [("Error: Invalid character '1' detected! Only Romanian alphabet letters and spaces are allowed.", (243, 139, 168))],
    ]
    render_terminal("caesar1.py — Invalid Character Validation", lines4, "report/images/caesar1_invalid_char.png")

    # 5. Caesar 2 Encrypt
    lines5 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar2.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("1", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("criptografie si securitate", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("7", (249, 226, 175))],
        [("Enter the keyword (string key, min 7 chars): ", (205, 214, 244)), ("universitate", (249, 226, 175))],
        [("Standard alphabet: ", (180, 190, 254)), ("aăâbcdefghiiîjklmnopqrsștțuvwxyz", (205, 214, 244))],
        [("Permuted alphabet: ", (180, 190, 254)), ("universtaăâbcdfeghîjklmopqștțwxyz", (205, 214, 244))],
        [("Encrypted text: ", (180, 190, 254)), ("bwîșzqgwtfîd xî xdbnwîztzd", (166, 227, 161))],
    ]
    render_terminal("caesar2.py — Permuted Alphabet Encryption", lines5, "report/images/caesar2_encrypt.png")

    # 6. Caesar 2 Decrypt
    lines6 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar2.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("2", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("bwîșzqgwtfîd xî xdbnwîztzd", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("7", (249, 226, 175))],
        [("Enter the keyword (string key, min 7 chars): ", (205, 214, 244)), ("universitate", (249, 226, 175))],
        [("Standard alphabet: ", (180, 190, 254)), ("aăâbcdefghiiîjklmnopqrsștțuvwxyz", (205, 214, 244))],
        [("Permuted alphabet: ", (180, 190, 254)), ("universtaăâbcdfeghîjklmopqștțwxyz", (205, 214, 244))],
        [("Decrypted text: ", (180, 190, 254)), ("criptografie si securitate", (166, 227, 161))],
    ]
    render_terminal("caesar2.py — Permuted Alphabet Decryption", lines6, "report/images/caesar2_decrypt.png")

    # 7. Caesar 2 Keyword Too Short
    lines7 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar2.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("1", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("criptografie", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("7", (249, 226, 175))],
        [("Enter the keyword (string key, min 7 chars): ", (205, 214, 244)), ("cheie", (249, 226, 175))],
        [("Error: Keyword is too short! It must be at least 7 characters long.", (243, 139, 168))],
    ]
    render_terminal("caesar2.py — Keyword Too Short Validation", lines7, "report/images/caesar2_short_keyword.png")

    # 8. Caesar 2 Invalid Characters / Key
    lines8 = [
        [("ilie@archlinux:~/CS/lab1$ ", (166, 227, 161)), ("python3 caesar2.py", (137, 220, 235))],
        [("Choose the operation:", (205, 214, 244))],
        [("1. Encrypt", (205, 214, 244))],
        [("2. Decrypt", (205, 214, 244))],
        [("Operation (1/2): ", (205, 214, 244)), ("1", (249, 226, 175))],
        [("Enter the text: ", (205, 214, 244)), ("criptografie", (249, 226, 175))],
        [("Enter the numeric key (1-30): ", (205, 214, 244)), ("0", (249, 226, 175))],
        [("Error: Invalid key! The numeric key must be an integer between 1 and 30.", (243, 139, 168))],
    ]
    render_terminal("caesar2.py — Invalid Key Validation", lines8, "report/images/caesar2_invalid_key.png")


if __name__ == "__main__":
    main()
