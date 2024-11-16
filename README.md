# Web-based-Encryption-and-Decryption
This project provides secure text encryption and decryption using AES encryption and QR code-based multi-factor authentication. It encrypts text with AES, then encodes both the AES key and ciphertext into QR codes for secure storage and transfer. The decryption process requires scanning the QR codes to retrieve the key and message.


AES Encryption and QR Code-Based Multi-Factor Authentication for Secure Text Encryption/Decryption

This repository provides a secure solution for encrypting and decrypting text using AES (Advanced Encryption Standard) encryption, paired with QR code-based multi-factor authentication (MFA). The combination of AES encryption and QR code-based authentication ensures that sensitive data is protected at all stages of the process, from encryption to decryption.

Key Features:
-->AES Encryption: Utilizes AES to encrypt text, providing a strong level of encryption for sensitive information.
-->Multi-Factor Authentication: Both the AES key and the encrypted text are stored in QR codes, requiring physical access to both QR codes for decryption.
-->Easy to Use: The system allows users to encrypt and decrypt messages with a passkey and QR code scanning, making it secure yet simple to use.
-->Cross-Platform: Can be used on any platform that supports QR code scanning and AES encryption libraries.
-->Secure Storage and Transfer: AES keys and encrypted messages are encoded into QR codes, making them easily shareable and securely stored.

Workflow:
1. Encryption:
    -->User enters a plain text message.
    -->A passkey is used to generate an AES encryption key.
    -->The message is encrypted using AES encryption.
    -->Both the AES key and the encrypted text are encoded into QR codes for secure transmission.
2. Decryption:
    -->User scans the QR codes to retrieve the AES key and encrypted text.
    -->The AES key is used to decrypt the ciphertext back into the original message.

Usage:
      -->Run the encryption_process.py file to encrypt text.
      -->Scan the QR codes generated during encryption to retrieve the AES key and ciphertext for decryption.
      -->Run the decryption_process.py file to decrypt the text using the AES key and the QR code.

Technologies Used:
    -->AES Encryption: For secure encryption of text.
    -->QR Codes: To securely store and transfer encryption keys and ciphertext.
    -->Python Libraries: cryptography, opencv-python, pyqrcode for QR code generation and encryption.
