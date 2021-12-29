alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "


def encrypt():
    text = input("Enter your text:")
    encrypted = ""
    for char in text:
        encrypted += alphabets[alphabets.index(char) + 21]
    print("Encrypted Text: \"" + encrypted + "\"")


def decrypt():
    text = input("Enter your text:")
    decrypted = ""
    for char in text:
        decrypted += alphabets[alphabets.index(char) - 21]
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
