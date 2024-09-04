"""
To check if it works, write a different Python program 
that opens the file, decodes the data and prints the content 
(should be the string we got as input in the first step.)
"""
with open("minfil.txt", "rb") as file:
    content = file.read()

decodedString = content.decode('UTF-8')
print(decodedString)