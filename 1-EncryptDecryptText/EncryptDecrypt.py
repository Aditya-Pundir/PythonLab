import base64


def encrypt():
    text = input("Enter your text:").encode("ascii")
    encrypted_bytes = base64.b64encode(text)
    encrypted = encrypted_bytes.decode("ascii")
    print("Encrypted Text: \"" + encrypted + "\"")


def decrypt():
    text = input("Enter your text:").encode("ascii")
    decrypted_bytes = base64.b64decode(text)
    decrypted = decrypted_bytes.decode("ascii")
    print("Decrypted Text: \"" + decrypted + "\"")


while __name__ == "__main__":
    print("Enter:")
    print("\t1 to encrypt")
    print("\t2 to decrypt")
    choice = int(input("here:"))

    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        print("Please enter a valid choice")
