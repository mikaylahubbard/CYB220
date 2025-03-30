plaintext = input("What phrase would you like to encrypt?: ")
length = len(plaintext)

#populate it with none
ciphertext = [None] * length
positions = []

for character in plaintext:
    message = f"""
    Where would you like to put the character {character}?: 
    """
    #a list of all the spots that are still None
    indicis = [i for i, x in enumerate(ciphertext) if x == None]
    valid_choice = False
    print()
    while valid_choice is False:
        print(indicis)
        print("Select any of the above values")
        new_position = int(input(message))
        print()
        if new_position in indicis:
            ciphertext[new_position] = character
            valid_choice = True
            positions.append(new_position)
        else:
            print("PLease enter a valid position")

ciphertext = ''.join(ciphertext)
print(f"Here are the new positions of each original character: {positions}")
print("..........................")
print(ciphertext)

