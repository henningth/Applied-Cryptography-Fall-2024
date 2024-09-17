"""
Write a function which encrypts a plaintext using AES in ECB mode
Plaintext length: Multiple of 16 byte (16, 32, 48, etc.)
Use the Cryptography library
Generate the key in a proper manner (cf. Last lecture)
Takes key and plaintext as input, return ciphertext

Write a function which decrypts a ciphertext using AES in ECB mode
Ciphertext length: Multiple of 16 bytes
Also use the Cryptography library
Takes key and ciphertext as input, return plaintext

Check whether the encryption is correct
Must be able to decrypt what was encrypted, given key
"""

import os # For generating a key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(16)

def encrypt(key, plaintext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    ciphertext += encryptor.finalize()
    return ciphertext

def decrypt(key, ciphertext):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())
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