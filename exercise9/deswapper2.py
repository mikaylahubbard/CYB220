ciphertext = input("What string would you like to decrypt?: ")
length = len(ciphertext)

active = True
while active is True:
    plaintext = [None] * length
    for character in ciphertext:
        message = f"""
        where would you like to put the character {character}?
        """
        indicis = [i for i, x in enumerate(plaintext) if x == None]
        valid_choice = False
        print()
        while valid_choice is False:
            print(indicis)
            print('Select any of the above values')
            new_position = int(input(message))
            print()
            if new_position in indicis:
                plaintext[new_position] = character
                valid_choice = True
            else:
                print("Please enter a valid position")

    plaintext = ''.join(plaintext)
    print("Here is the decryptted text:")
    print(plaintext)
    again = input("Would you like to trya a different combination (y/n)?: ")
    if again.lower() == "y":
        continue
    elif again.lower() == "n":
        active = False

