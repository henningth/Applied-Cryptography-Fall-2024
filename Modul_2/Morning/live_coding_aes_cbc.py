"""
Write a Python program which can encrypt and decrypt using AES in CBC mode
Plaintext length: Multiple of 16 bytes

Use Cryptography library in Python

Test if implementation is valid
Must be able to decrypt ciphertext back to original

Test if implementation is secure
Ciphertext should look random
"""

import os # For generating a key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(16)
iv = os.urandom(16)

def encrypt(key, plaintext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    ciphertext += encryptor.finalize()
    return ciphertext

def decrypt(key, ciphertext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    decryptor = cipher.decryptor()
    decryptedtext = decryptor.update(ciphertext)
    decryptedtext += decryptor.finalize()
    return decryptedtext

plaintext = b'Hello AES World.Hello AES World.Hello AES World.'
ciphertext = encrypt(key, plaintext)
print(ciphertext)

decryptedtext = decrypt(key, ciphertext)
#print(decryptedtext)
if decryptedtext == plaintext:
    print("SUCCESS")
else:
    print("FAIL")