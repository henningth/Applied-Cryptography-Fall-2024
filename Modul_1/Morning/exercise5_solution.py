"""
Exercise 5: Write a Python program that opens a PNG file in 
binary mode and prints the first 8 bytes of the file (its signature). 
Compare with https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header
"""

with open("C:\Projects\Applied-Cryptography-Fall-2024\Modul_1\Morning\dice.png", "rb") as file:
    content = file.read(8)

print(content)