# Importing the 'derive_key_from_passkey' function from the 'encryption_module', which is used to derive a cryptographic key from a user-provided passkey for decryption.
# Importing 'aes_decrypt' from the 'encryption_module' to decrypt the encrypted text using the AES algorithm.
from encryption_module import derive_key_from_passkey, aes_decrypt
# Importing the 'base64' library to handle encoding and decoding of binary data in base64 format, especially for handling encrypted data and AES keys in text-based formats (QR codes).
import base64
# Importing the 'cv2' module (OpenCV) to handle image processing tasks, specifically for reading and decoding QR codes to extract information such as the AES key and encrypted text.
import cv2

#Reads a QR code and returns the decoded data.
def read_qr_code(file_path):
    
    # Reads the image from the given file path using OpenCV (cv2) and stores it in the 'img' variable.
    img = cv2.imread(file_path)

    # Creates a QRCodeDetector object from OpenCV, which will be used to detect and decode QR codes in the image.
    detector = cv2.QRCodeDetector()

    # Detects and decodes the QR code from the image. The 'data' variable contains the decoded string or data.
    # The '_,' parts are placeholders for unused values that detectAndDecode returns, like the points of the QR code.
    data, _, _ = detector.detectAndDecode(img)

    if not data:
        raise ValueError(f"Could not decode QR code from {file_path}.")
    return data


#    Manages the decryption process: user input, decryption, and output display.
def decryption_process():
    key_qr_path = input("Enter the path of the AES key QR code: ")
    cipher_text_qr_path = input("Enter the path of the encrypted text QR code: ")

    passkey = input("Enter the same passkey used during encryption: ")
    aes_key = derive_key_from_passkey(passkey)

    try:
        # Decode QR codes
        aes_key_decoded = base64.b64decode(read_qr_code(key_qr_path))  # Decode the base64 QR code to get the byte array
        cipher_text = read_qr_code(cipher_text_qr_path)
        # Perform decryption
        decrypted_text = aes_decrypt(cipher_text, aes_key_decoded)
        print(f"Decrypted text: {decrypted_text}")

    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    decryption_process()
