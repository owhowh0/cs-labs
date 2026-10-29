import sys

ROMANIAN_ALPHABET = [
    "A", "Ă", "Â", "B", "C", "D", "E", "F", "G", "H", "I", "Î", "J", "K",
    "L", "M", "N", "O", "P", "Q", "R", "S", "Ș", "T", "Ț", "U", "V", "W",
    "X", "Y", "Z"
]


PLAYFAIR_ALPHABET = [
    "A", "Ă", "Â", "B", "C", "D", "E", "F", "G", "H", "I", "Î", "K",
    "L", "M", "N", "O", "P", "Q", "R", "S", "Ș", "T", "Ț", "U", "V", "W",
    "X", "Y", "Z"
]

MATRIX_ROWS = 6
MATRIX_COLS = 5


def normalize_character(char: str) -> str:
    cedilla_map = {
        "\u015e": "\u0218",  # Ş -> Ș
        "\u015f": "\u0219",  # ş -> ș
        "\u0162": "\u021a",  # Ţ -> Ț
        "\u0163": "\u021b",  # ţ -> ț
    }
    char = cedilla_map.get(char, char)
    return char.upper()


def validate_keyword(keyword: str) -> bool:
    if not keyword:
        print("Error: Keyword cannot be empty.")
        return False

    clean_key = keyword.strip()
    if len(clean_key) < 7:
        print(f"Error: Keyword is too short ({len(clean_key)} chars)! It must be at least 7 characters long.")
        return False

    for char in clean_key:
        norm = normalize_character(char)
        if norm not in ROMANIAN_ALPHABET and norm != " ":
            print(f"Error: Invalid character '{char}' in keyword!")
            print("Allowed characters: A-Z, Ă, Â, Î, Ș, Ț (letters only, min length 7).")
            return False

    return True


def validate_text(text: str) -> bool:
    if not text or not text.strip():
        print("Error: Input text cannot be empty.")
        return False

    for char in text:
        norm = normalize_character(char)
        if norm not in ROMANIAN_ALPHABET and norm != " ":
            print(f"Error: Invalid character '{char}' detected!")
            print("Allowed characters: letters from Romanian alphabet (A-Z, a-z, ă, â, î, ș, ț) and spaces.")
            return False

    return True


def build_matrix(keyword: str):
    unique_key = []
    for char in keyword:
        norm = normalize_character(char)
        if norm == " ":
            continue
        c = "I" if norm == "J" else norm
        if c in PLAYFAIR_ALPHABET and c not in unique_key:
            unique_key.append(c)

    for char in PLAYFAIR_ALPHABET:
        if char not in unique_key:
            unique_key.append(char)

    matrix = [unique_key[i:i + MATRIX_COLS] for i in range(0, len(unique_key), MATRIX_COLS)]

#    matrix = []
#    for i in range(0, len(unique_key), MATRIX_COLS):
#        row = unique_key[i:i + MATRIX_COLS]
#        matrix.append(row)
    return matrix


def print_matrix(matrix):
    print("Playfair Matrix (6x5):")
    print("  +----+----+----+----+----+")
    for row in matrix:
        formatted_cells = " | ".join(f"{c:^2}" for c in row)
        print(f"  | {formatted_cells} |")
        print("  +----+----+----+----+----+")


def get_char_positions(matrix):
    pos = {}
    for r in range(MATRIX_ROWS):
        for c in range(MATRIX_COLS):
            pos[matrix[r][c]] = (r, c)
    return pos


def prepare_plaintext(text: str):
    clean = []
    for char in text:
        norm = normalize_character(char)
        if norm == " ":
            continue
        c = "I" if norm == "J" else norm
        if c in PLAYFAIR_ALPHABET:
            clean.append(c)

    pairs = []
    i = 0
    n = len(clean)
    while i < n:
        first = clean[i]
        if i + 1 < n:
            second = clean[i + 1]
            if first == second:
                filler = "Z" if first == "X" else "X"
                pairs.append((first, filler))
                i += 1
            else:
                pairs.append((first, second))
                i += 2
        else:
            filler = "Z" if first == "X" else "X"
            pairs.append((first, filler))
            i += 1

    return pairs


def prepare_ciphertext(text: str):
    clean = []
    for char in text:
        norm = normalize_character(char)
        if norm == " ":
            continue
        c = "I" if norm == "J" else norm
        if c in PLAYFAIR_ALPHABET:
            clean.append(c)

    if len(clean) % 2 != 0:
        print("Warning: Ciphertext has an odd number of characters. Appending 'X' padding.")
        clean.append("X")

    pairs = [(clean[i], clean[i + 1]) for i in range(0, len(clean), 2)]
    return pairs


def encrypt_pair(matrix, pos, p1: str, p2: str):
    r1, c1 = pos[p1]
    r2, c2 = pos[p2]

    if r1 == r2:
        # Same row: shift right circularly
        return matrix[r1][(c1 + 1) % MATRIX_COLS] + matrix[r2][(c2 + 1) % MATRIX_COLS]
    elif c1 == c2:
        # Same column: shift down circularly
        return matrix[(r1 + 1) % MATRIX_ROWS][c1] + matrix[(r2 + 1) % MATRIX_ROWS][c2]
    else:
        # Rectangle rule: exchange column indices
        return matrix[r1][c2] + matrix[r2][c1]


def decrypt_pair(matrix, pos, c1: str, c2: str):
    r1, col1 = pos[c1]
    r2, col2 = pos[c2]

    if r1 == r2:
        # Same row: shift left circularly
        return matrix[r1][(col1 - 1) % MATRIX_COLS] + matrix[r2][(col2 - 1) % MATRIX_COLS]
    elif col1 == col2:
        # Same column: shift up circularly
        return matrix[(r1 - 1) % MATRIX_ROWS][col1] + matrix[(r2 - 1) % MATRIX_ROWS][col2]
    else:
        # Rectangle rule: exchange column indices
        return matrix[r1][col2] + matrix[r2][col1]


def encrypt(plaintext: str, keyword: str):
    matrix = build_matrix(keyword)
    pos = get_char_positions(matrix)
    pairs = prepare_plaintext(plaintext)

    cipher_pairs = [encrypt_pair(matrix, pos, p1, p2) for p1, p2 in pairs]
    ciphertext = "".join(cipher_pairs)
    return ciphertext, pairs, cipher_pairs, matrix


def decrypt(ciphertext: str, keyword: str):
    matrix = build_matrix(keyword)
    pos = get_char_positions(matrix)
    pairs = prepare_ciphertext(ciphertext)

    plain_pairs = [decrypt_pair(matrix, pos, c1, c2) for c1, c2 in pairs]
    plaintext_raw = "".join(plain_pairs)
    return plaintext_raw, pairs, plain_pairs, matrix



def main():
    print("Playfair Cipher")
    print("Choose the operation:")
    print("1. Encrypt")
    print("2. Decrypt")
    operation = input("Operation (1/2): ").strip()

    if operation not in ["1", "2"]:
        print("Error: Invalid operation choice! Please select 1 or 2.")
        return

    text = input("Enter the text: ").strip()
    if not validate_text(text):
        return

    keyword = input("Enter the keyword (min 7 chars): ").strip()
    if not validate_keyword(keyword):
        return

    if operation == "1":
        ciphertext, plain_pairs, cipher_pairs, matrix = encrypt(text, keyword)
        print_matrix(matrix)
        print("Plaintext Digraphs :", " ".join(f"{p[0]}{p[1]}" for p in plain_pairs))
        print("Cipher Digraphs    :", " ".join(cipher_pairs))
        print("Encrypted text     :", ciphertext)
    else:
        plaintext_raw, cipher_pairs, plain_pairs, matrix = decrypt(text, keyword)
        print_matrix(matrix)
        print("Cipher Digraphs    :", " ".join(f"{p[0]}{p[1]}" for p in cipher_pairs))
        print("Decrypted Digraphs :", " ".join(f"{p[0]}{p[1]}" for p in plain_pairs))
        print("Decrypted text     :", plaintext_raw)


if __name__ == "__main__":
    main()

