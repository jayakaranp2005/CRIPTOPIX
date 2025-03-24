# CRIPTOPIX

CRIPTOPIX is a Python-based application that allows users to encrypt and decrypt images using the Fernet symmetric encryption method. The application provides a graphical user interface (GUI) built with Tkinter, making it easy for users to select, encrypt, and decrypt images.

## Features

- **Image Encryption**: Encrypt images with a Fernet key to secure sensitive information.
- **Image Decryption**: Decrypt encrypted images using the corresponding Fernet key.
- **Key Management**: Generate and save Fernet keys for encryption and decryption.
- **User-Friendly Interface**: Simple and intuitive GUI for easy interaction.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `tkinter`
  - `Pillow`
  - `cryptography`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/jayakaranp2005/CRIPTOPIX.git
   cd CRIPTOPIX
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```sh
   python tklearn.py
   ```

2. The GUI will open, allowing you to select an image to encrypt or decrypt.

3. **Encrypt Image**:
   - Click on the "Encrypt Image" button.
   - The application will generate a Fernet key and encrypt the selected image.

4. **Decrypt Image**:
   - Enter the Fernet key in the provided field.
   - Click on the "Decrypt Image" button.
   - The application will decrypt the image using the provided key.

## Project Structure

- `tklearn.py`: Main GUI application file.
- `enc.py`: Handles image encryption.
- `denc.py`: Handles image decryption.
- `fernet_key.key`: File to store the generated Fernet key.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
