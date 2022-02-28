from steganocryptopy.steganography import Steganography


def encrypt(key, image, data, location):
    # Encrypts the key every time something is encoded
    Steganography.generate_key(key)
    encrypted = Steganography.encrypt(key, image, data)
    encrypted.save(location)


def decrypt():
    decrypted = Steganography.decrypt("key.txt", "liberty.jpeg")
    print(decrypted)


def start():
    options = "Enter:\n\t1 to encode\n\t2 to decode\nhere: "
    choice = int(input(options))

    if choice == 1:
        image = input("Enter image location:")
        key = input("Enter key location:")
        data = input("Enter data location:")
        location = input("Enter location to save image to:")
        encrypt(key, image, data, location)
    elif choice == 2:
        # image = input("Enter image location:")
        # key = input("Enter key location:")
        decrypt()
    else:
        print("Enter a valid choice!")


while __name__ == "__main__":
    start()
