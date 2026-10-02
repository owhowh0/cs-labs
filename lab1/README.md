# CS Laboratory Works — Cryptography & Security

This repository contains the laboratory works for the **Computer Security / Cryptography** course at the **Technical University of Moldova (UTM)**, Faculty of Computers, Informatics and Microelectronics (FCIM).

- **Student:** Ilie Covali
- **Group:** FAF-243
- **Branch:** `lab1`

---

## Laboratory Work 1: Classical Cryptography
Implementation and analysis of classical monoalphabetic substitution ciphers over the Romanian alphabet ($N = 31$ letters):
1. **Standard Caesar Cipher (`caesar1.py`)**:
   - Modular shift operations $C = (P + k) \pmod{31}$ and $P = (C - k) \pmod{31}$.
   - Key space of size $|\mathcal{K}| = 30$ ($k \in [1, 30]$).
   - Strict input validation for numeric keys and invalid characters.
2. **Caesar Cipher with Keyword Permutation (`caesar2.py`)**:
   - Dynamic construction of a permuted alphabet $\Pi$ using a secret keyword ($K$, $\text{length} \ge 7$) and a secondary numeric shift $k \in [1, 30]$.
   - Bidirectional bijective mapping between the standard alphabet $\mathcal{A}$ and permuted alphabet $\Pi$.
   - Expanded key space exceeding $3.98 \times 10^{11}$ combinations.
   - Comprehensive input validation (rejecting short keywords, invalid characters, and degenerate shifts).

---

## Project Structure

```
.
├── caesar1.py                 # Task 1: Standard Caesar cipher implementation
├── caesar2.py                 # Task 2: Caesar cipher with permuted alphabet
├── generate_screenshots.py    # Automation script to render terminal execution figures
├── pyproject.toml             # Python project metadata
├── README.md                  # Project documentation
└── report/
    ├── labreport.cls          # Custom LaTeX document class
    ├── report.tex             # Full LaTeX report source
    ├── report.pdf             # Compiled lab report PDF
    ├── titlesec.sty           # LaTeX dependency
    └── images/                # Execution and error validation screenshot assets
        ├── caesar1_encrypt.png
        ├── caesar1_decrypt.png
        ├── caesar1_invalid_key.png
        ├── caesar1_invalid_char.png
        ├── caesar2_encrypt.png
        ├── caesar2_decrypt.png
        ├── caesar2_short_keyword.png
        └── caesar2_invalid_key.png
```

---

## How to Run

### Requirements
- Python 3.10+
- Optional for report compilation: TeX Live (`pdflatex`, `texlive-fontsrecommended`)

### Running the Programs

1. **Standard Caesar Cipher:**
   ```bash
   python3 caesar1.py
   ```
2. **Caesar Cipher with Permutation:**
   ```bash
   python3 caesar2.py
   ```

### Compiling the Report
```bash
cd report
pdflatex -interaction=nonstopmode report.tex
pdflatex -interaction=nonstopmode report.tex
```
