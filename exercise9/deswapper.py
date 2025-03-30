import math
import random
ciphertext = input("What string would you like to decrypt?: ")
length = len(ciphertext)
#print(length)
#calculate permutations of the string provided
numPermutations = math.factorial(length)
#print(numPermutations)

options = []
while  numPermutations > 0:
    positions = []
    plaintext = [None] * length
    #andomly swap letters around and add it to the list
    for character in ciphertext:
        valid_choice = False
        indicis = [i for i, x in enumerate(plaintext) if x == None]
        while valid_choice is False:
            new_position = random.choice(indicis)
            if new_position in indicis:
                plaintext[new_position] = character
                valid_choice = True
                positions.append(new_position)
    plaintext = ''.join(plaintext) 
    if plaintext not in options:
        options.append(plaintext)
        numPermutations -= 1;
    
        
 

print(f"Your Decrypted Message options: ")
for option in options:
    print(option)
