from PIL import Image
import random

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    #print(pixels)
    width, height = img.size

    random.seed(key)

    indices = list(range(len(pixels)))
    random.shuffle(indices)

    shuffled_pixels = [pixels[i] for i in indices]

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(shuffled_pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    shuffled_pixels = list(img.getdata())
    width, height = img.size

    random.seed(key)

    indices = list(range(len(shuffled_pixels)))
    random.shuffle(indices)

    original_pixels = [None] * len(shuffled_pixels)

    for original_index, shuffled_index in enumerate(indices):
        original_pixels[shuffled_index] = shuffled_pixels[original_index]

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(original_pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()

        if choice == 'q':
            print("*")
            print(" ")
            print("Exiting the Image Encryption and Decryption Tool. Stay secure!")
            print(" ")
            print("*")
            break

        elif choice == 'e':
            print("*")
            print(" ")
            print("Encryption")
            print(" ")
            print("*")
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter the secret key value for encryption: "))
            output_path = input("Enter the path to save the encrypted image: ")
            encrypt_image(image_path, key, output_path)

        elif choice == 'd':
            print("*")
            print(" ")
            print("Decryption")
            print(" ")
            print("*")
            image_path = input("Enter the path of the image to decrypt: ")
            key = int(input("Enter the secret key value for decryption: "))
            output_path = input("Enter the path to save the decrypted image: ")
            decrypt_image(image_path, key, output_path)

        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()