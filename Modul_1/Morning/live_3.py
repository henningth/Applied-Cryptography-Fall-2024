"""
Write a Python program which takes a string as input.
This string should be encoded to UTF-8
Then, save the string in a new file.
"""
string = input("Enter string: ")
encodedString = string.encode('UTF-8')

with open("minfil.txt", "wb") as file:
    file.write(encodedString)