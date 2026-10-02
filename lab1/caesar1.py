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


def validate_text(text):
    if not text:
        print("Error: Input text cannot be empty.")
        return False
    for char in text:
        if char not in alphabet and char != " ":
            print(f"Error: Invalid character '{char}' detected! Only Romanian alphabet letters and spaces are allowed.")
            return False
    return True


def encrypt(text, key):
    result = ""
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + key) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    print("Encrypted text:", result)
    return result


def decrypt(text, key):
    result = ""
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) - key) % len(alphabet)
            result += alphabet[new_index]
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
    key = validate_key(key_input)
    if key is None:
        return

    if operation == "1":
        encrypt(text, key)
    else:
        decrypt(text, key)


if __name__ == "__main__":
    main()
