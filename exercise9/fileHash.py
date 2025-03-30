import hashlib

filename1 = input("Enter a filename: ")
filename2 = input("Enter a second filename: ")

file1 = open(filename1, "r").read().strip()
hash1 = hashlib.sha256(file1.encode()).hexdigest()

file2 = open(filename2, "r").read().strip()
hash2 = hashlib.sha256(file2.encode()).hexdigest()

print("hashes:")
print(hash1)
print(hash2)

if hash1 == hash2:
    print("The files are the same!")
else:
    print("the files are not the same")
