# Importing necessary functions from the 'encryption_module' to handle passkey derivation, AES encryption, and QR code generation.
from encryption_module import derive_key_from_passkey, aes_encrypt, generate_qr_code
# Importing the base64 library to handle encoding and decoding of binary data in base64 format, especially for QR code generation and encryption processes.
import base64

# Manages the encryption process: user input, encryption, and QR code generation.
def encryption_process():

    plain_text = input("Enter the text you want to encrypt: ")

    # Get passkey and derive cryptographic key
    passkey = input("Enter a secure passkey (10-20 characters with letters, numbers, and special characters): ")
    aes_key = derive_key_from_passkey(passkey)

    # Encrypt the plain text
    cipher_text = aes_encrypt(plain_text, aes_key)

    # Generate QR codes for key and ciphertext
    # Generate a QR code for the AES encryption key, which is first encoded in base64 format to ensure it's in a safe, text-based form suitable for QR encoding.
    # The 'return_buffer=True' option returns the QR code as a buffer (an image object in memory) instead of saving it to a file.
    key_qr_buffer = generate_qr_code(base64.b64encode(aes_key), return_buffer=True)  
    # Generate a QR code for the encrypted text (cipher_text), encoding it to bytes before passing it to the QR code generation function.
    text_qr_buffer = generate_qr_code(cipher_text.encode(), return_buffer=True)

    print("Encryption complete. Save the QR codes securely.")
    return qr_key, qr_text

if __name__ == "__main__":
    encryption_process()
