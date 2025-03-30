plaintext = input("What phrase would you like to encrypt?: ")
length = len(plaintext)

message = f"""
Qfter how many characters would you like the split to happen> Enter a number between 1 and {length-1}: 
"""
splitter = int(input(message))

ciphertext = ""
ciphertext = plaintext[splitter:] + plaintext[:splitter]

print(ciphertext)
