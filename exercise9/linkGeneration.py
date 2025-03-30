import string
import secrets

header = "https://teameffort.work/"
footer = ".png"

letters = string.ascii_letters + string.digits
urls = []

for x in range(100): 
    randString = ''
    for y in range(12):
        randString += secrets.choice(letters)
    url = header + randString + footer
    urls.append(url)


print(len(urls))
for url in urls:
    print(url)
