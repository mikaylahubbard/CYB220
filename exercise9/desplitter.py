ciphertext = input("Enter the string you would like to decrypt: ")
length = len(ciphertext)

print("Testing different split options. The answer should be in this list:")

for num in range(1, length-1):
    plaintext = ciphertext[num:] + ciphertext[:num]
    print(plaintext)

