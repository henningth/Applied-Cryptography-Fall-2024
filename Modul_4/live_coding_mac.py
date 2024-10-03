"""
Write a program in Python which computes the MAC of some 
given data and a secret key
Use HMAC in the Cryptography module
Write it as a function computeTag(m,k), which returns the tag

Add a function verifyTag(m, t, k) which takes message m, 
tag t and key k as input, and returns True or False 
depending on whether tag is valid (=not tampered with)
"""

from cryptography.hazmat.primitives import hashes, hmac
from os import urandom

message = b'Yellow Submarine'
key = urandom(16)

def computeTag(m,k):
    h = hmac.HMAC(k, hashes.SHA256())
    h.update(m)
    tag = h.finalize()
    return tag

def verifyTag(m, t, k):
    h = hmac.HMAC(k, hashes.SHA256())
    h.update(m)
    computedTag = h.finalize()
    if t == computedTag:
        return True
    else:
        return False

# Testing computeTag
tag = computeTag(message, key)
print(tag)

# Testing verifyTag
result = verifyTag(message, tag, key)
print(result)