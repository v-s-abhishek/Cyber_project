from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    """Encrypt an image using pixel manipulation."""
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a NumPy array
    pixels = np.array(image)

    # Perform pixel manipulation based on the key
    rows, cols, _ = pixels.shape
    for i in range(rows):
        for j in range(cols):
            pixels[i, j, 0] = (pixels[i, j, 0] + key) % 256
            pixels[i, j, 1] = (pixels[i, j, 1] * key) % 256
            pixels[i, j, 2] = (pixels[i, j, 2] - key) % 256

    # Create a new image from the modified pixel array
    encrypted_image = Image.fromarray(pixels.astype(np.uint8))
    return encrypted_image

def decrypt_image(image_path, key):
    """Decrypt an image using pixel manipulation."""
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a NumPy array
    pixels = np.array(image)

    # Perform the reverse pixel manipulation based on the key
    rows, cols, _ = pixels.shape
    for i in range(rows):
        for j in range(cols):
            pixels[i, j, 0] = (pixels[i, j, 0] - key) % 256
            pixels[i, j, 1] = (pixels[i, j, 1] // key) % 256
            pixels[i, j, 2] = (pixels[i, j, 2] + key) % 256

    # Create a new image from the modified pixel array
    decrypted_image = Image.fromarray(pixels.astype(np.uint8))
    return decrypted_image

image_path = input("Enter the path to the image: ")
key = int(input("Enter the encryption/decryption key: "))

encrypted_image = encrypt_image(image_path, key)
encrypted_image.save("encrypted_image.png")
print("Encrypted image saved as 'encrypted_image.png'.")

decrypted_image = decrypt_image("encrypted_image.png", key)
decrypted_image.save("decrypted_image.png")
print("Decrypted image saved as 'decrypted_image.png'.")