from PIL import Image
from cryptography.fernet import Fernet
import io
from tkinter import Tk, filedialog

def generate_and_save_key():
    key = Fernet.generate_key()
    key_path = 'fernet_key.key'
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    print(f"Fernet Key saved to '{key_path}'.")

def load_key(key_path='fernet_key.key'):
    # Read the key from the file
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_data(data, key):
    # Create a Fernet object with the key
    fernet = Fernet(key)
    # Encrypt the data
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def select_image():
    # Initialize Tkinter root
    root = Tk()
    root.withdraw()  # Hide the root window
    # Open file dialog to select an image
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    root.destroy()  # Destroy the root window
    if not filepath:
        raise FileNotFoundError("No file selected.")
    return filepath

def main():
    # Uncomment the line below to generate a new key (run this once)
    generate_and_save_key()

    # Load the Fernet key
    key = load_key()

    # Select an image file
    image_path = select_image()

    # Open the image file
    with Image.open(image_path) as img:
        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        img_bytes = img_byte_arr.getvalue()

    # Encrypt the image bytes
    encrypted_data = encrypt_data(img_bytes, key)

    # Save the encrypted data to a file
    with open('encrypted_image.enc', 'wb') as enc_file:
        enc_file.write(encrypted_data)

    print("Image encrypted and saved to 'encrypted_image.enc'.")

if __name__ == "__main__":
    main()
