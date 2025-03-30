import hashlib

hash = open("hash.txt", "r").read().strip()

print("Attempting to crack the following hash:")
print(hash)
print("................................................")

active = True
while active == True:
    attempt = input("Enter a string to test: ")
    attempt_hash = hashlib.sha256(attempt.strip().encode()).hexdigest()
    if attempt_hash == hash:
        print("Correct! The hashes are a match!")
        active = False
    else:
        again = input("Alas, the hashes do not match. Try again? (y/n): ")
        if again.lower() == "n":
            active = False

