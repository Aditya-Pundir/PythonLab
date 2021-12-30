from steganocryptopy.steganography import Steganography


def encrypt(key, image, data, location):
    Steganography.generate_key(key)
    encrypted = Steganography.encrypt(key, image, data)
    encrypted.save(location)


def decrypt(key, image):
    print(Steganography.decrypt(key, image))


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
        image = input("Enter image location:")
        key = input("Enter key location:")
        decrypt(key, image)
    else:
        print("Enter a valid choice!")


while __name__ == "__main__":
    start()
