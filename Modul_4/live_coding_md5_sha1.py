"""
Write a Python program which computes the SHA-1 and MD5 hashes of a given bytearray 
Test with various fixed bytearrays: b’Yellow Submarine’ for example

Use Cryptography library in Python

Test for the avalanche effect
Small change in input gives large change in output
"""

from cryptography.hazmat.primitives.hashes import Hash, MD5, SHA256

# Input data
inputData = b'Yellow Submarine'

# Compute MD5 digest
hash = Hash(SHA256())
hash.update(inputData)
md5hash = hash.finalize()
print(md5hash)
#print(len(md5hash))

print("--------------------------------------\n")
inputData = b'Yellow submarine'
# Compute MD5 digest
hash = Hash(SHA256())
hash.update(inputData)
md5hash = hash.finalize()
print(md5hash)

# Compute SHA1 digest