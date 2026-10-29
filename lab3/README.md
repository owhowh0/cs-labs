# CS Laboratory Works — Cryptography & Security

This repository contains the laboratory works for the **Computer Security / Cryptography** course at the **Technical University of Moldova (UTM)**, Faculty of Computers, Informatics and Microelectronics (FCIM).

- **Student:** Ilie Covali
- **Group:** FAF-243
- **Branch:** `main`

---

## Laboratory Work 3: Polyalphabetic Ciphers
Implementation and mathematical formalization of classical polygraphic/polyalphabetic ciphers.

### Task 3.1: The Playfair Cipher Adapted for the Romanian Alphabet ($N = 31$ letters)
1. **$6 \times 5$ Matrix Topology:**
   - Adapts the classical $5 \times 5$ Wheatstone-Playfair grid to the Romanian alphabet ($N = 31$ characters).
   - In accordance with the laboratory guidelines, the infrequent letter `J` is merged into `I` ($J \to I$), yielding exactly 30 unique symbols that populate a $6 \times 5$ rectangular grid:
     $$\mathcal{A}_{\text{playfair}} = [\text{A, Ă, Â, B, C, D, E, F, G, H, I, Î, K, L, M, N, O, P, Q, R, S, Ș, T, Ț, U, V, W, X, Y, Z}]$$
2. **Digraph Preprocessing & Collision Handling:**
   - Spaces and non-alphabetic characters stripped; text converted to uppercase.
   - Digraph partitioning with automatic filler insertion (`'X'`, or `'Z'` if duplicate character is `'X'`) between identical letters in a pair.
   - Terminal padding with `'X'` (or `'Z'`) for odd-length strings.
3. **Cryptographic Transformations:**
   - **Same Row:** Circular shift right for encryption ($c \to (c + 1) \pmod 5$), circular shift left for decryption ($c \to (c - 1) \pmod 5$).
   - **Same Column:** Circular shift down for encryption ($r \to (r + 1) \pmod 6$), circular shift up for decryption ($r \to (r - 1) \pmod 6$).
   - **Rectangle Rule:** Swap column coordinates ($(r_1, c_2)$ and $(r_2, c_1)$).
4. **Defensive Input Validation:**
   - Rejection of keywords shorter than 7 characters ($\operatorname{length}(K) \ge 7$).
   - Rejection of invalid characters (digits, symbols, punctuation) with suggestions indicating the permitted Romanian character range.
5. **Decryption & Whitespace Handling:**
   - Decryption with the known secret key is strictly deterministic and reconstructs the exact plaintext character stream.
   - Per laboratory instructions, final whitespace restoration is performed manually based on sentence logic and language context.

---

## Project Structure

```
.
├── playfair.py                # Task 3.1: Playfair cipher implementation & interactive CLI
├── generate_screenshots.py    # Automation script rendering terminal execution figures
├── pyproject.toml             # Python project metadata (managed with uv)
├── uv.lock                    # Dependency lockfile
├── README.md                  # Project documentation
└── report/
    ├── labreport.cls          # Custom LaTeX document class
    ├── report.tex             # Full LaTeX report source
    ├── report.pdf             # Compiled lab report PDF
    ├── titlesec.sty           # LaTeX dependency
    └── images/                # Terminal execution and validation screenshot assets
        ├── playfair_encrypt_ro.png
        ├── playfair_decrypt_ro.png
        ├── playfair_encrypt_en.png
        ├── playfair_decrypt_en.png
        ├── playfair_invalid_key_short.png
        ├── playfair_invalid_char.png
        └── playfair_invalid_op.png
```

---

## How to Run

### Requirements
- Python 3.10+ (managed via `uv` or standard Python)
- Dependencies: `pillow` (for screenshot generation)
- Optional for report compilation: TeX Live (`pdflatex`, `texlive-fontsrecommended`)

### Environment Setup

Using `uv`:
```bash
cd lab3
uv sync
```

### Running the Cipher Program

Interactive mode:
```bash
uv run python playfair.py
```
Or with standard Python:
```bash
python3 playfair.py
```

### Generating Terminal Screenshot Figures

```bash
uv run python generate_screenshots.py
```

### Compiling the LaTeX Report

```bash
cd report
pdflatex -interaction=nonstopmode report.tex
pdflatex -interaction=nonstopmode report.tex
```
