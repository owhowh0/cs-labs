alphabet = [
    "a", "ă", "â", "b", "c", "d", "e", "f", "g", "h", "i", "î", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "ș", "t", "ț", "u", "v", "w",
    "x", "y", "z"
]


def validate_key(key_input):
    try:
        key = int(key_input)
        if 1 <= key < len(alphabet):
            return key
        else:
            print(f"Error: Invalid key! The numeric key must be an integer between 1 and {len(alphabet) - 1}.")
            return None
    except ValueError:
        print("Error: Invalid key! Key must be an integer number.")
        return None


def validate_keyword(keyword):
    if len(keyword) < 7:
        print("Error: Keyword is too short! It must be at least 7 characters long.")
        return False
    for char in keyword:
        if char not in alphabet:
            print(f"Error: Invalid character '{char}' in keyword! Only Romanian alphabet letters are allowed (no spaces or numbers).")
            return False
    return True


def validate_text(text):
    if not text:
        print("Error: Input text cannot be empty.")
        return False
    for char in text:
        if char not in alphabet and char != " ":
            print(f"Error: Invalid character '{char}' detected! Only Romanian alphabet letters and spaces are allowed.")
            return False
    return True


def build_permuted_alphabet(keyword):
    unique_key = []
    for char in keyword:
        if char not in unique_key:
            unique_key.append(char)
    remaining = [char for char in alphabet if char not in unique_key]
    return unique_key + remaining


def encrypt(text, numeric_key, permuted_alphabet):
    result = ""
    for char in text:
        if char in alphabet:
            plain_index = alphabet.index(char)
            cipher_index = (plain_index + numeric_key) % len(alphabet)
            result += permuted_alphabet[cipher_index]
        else:
            result += char
    print("Encrypted text:", result)
    return result


def decrypt(text, numeric_key, permuted_alphabet):
    result = ""
    for char in text:
        if char in permuted_alphabet:
            cipher_index = permuted_alphabet.index(char)
            plain_index = (cipher_index - numeric_key) % len(alphabet)
            result += alphabet[plain_index]
        else:
            result += char
    print("Decrypted text:", result)
    return result


def main():
    print("Choose the operation:")
    print("1. Encrypt")
    print("2. Decrypt")
    operation = input("Operation (1/2): ").strip()

    if operation not in ["1", "2"]:
        print("Error: Invalid operation choice! Please select 1 or 2.")
        return

    text = input("Enter the text: ").strip().lower()
    if not validate_text(text):
        return

    key_input = input(f"Enter the numeric key (1-{len(alphabet) - 1}): ").strip()
    numeric_key = validate_key(key_input)
    if numeric_key is None:
        return

    keyword = input("Enter the keyword (string key, min 7 chars): ").strip().lower()
    if not validate_keyword(keyword):
        return

    permuted_alphabet = build_permuted_alphabet(keyword)
    print("Standard alphabet: ", "".join(alphabet))
    print("Permuted alphabet: ", "".join(permuted_alphabet))

    if operation == "1":
        encrypt(text, numeric_key, permuted_alphabet)
    else:
        decrypt(text, numeric_key, permuted_alphabet)


if __name__ == "__main__":
    main()
