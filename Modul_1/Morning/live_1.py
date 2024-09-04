number = 3

print(bin(number))
print(hex(number))

# XOR computation
a = int('0101', 2)
b = int('1101', 2)

print(a)
print(b)

axorb = a ^ b

print(axorb)
print(bin(axorb))

result = 0b0010 ^ 0b1101
print(result)
#result = '0010' ^ '1101'

"""
Define two bit strings 0b10110011 and 0b11011100

Compute on paper and in Python:

The bitwise AND of the two bitstrings
The bitwise OR of the two bitstrings
The bitwise XOR of the two bitstrings (especially important!)

"""
bitstring1 = 0b10110011
bitstring2 = 0b11011100

bit1andbit2 = bitstring1 & bitstring2 # AND
bit1orbit2 = bitstring1 | bitstring2 # OR
bit1xorbit2 = bitstring1 ^ bitstring2 # XOR

print(bin(bit1andbit2))
print(bin(bit1orbit2))
print(bin(bit1xorbit2))