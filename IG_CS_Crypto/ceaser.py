myLetters = []
ordLetters = []
ordEncrypted = []
encryptedLetters = []
shiftKey = 0

myWord = input("Enter a word: ")
shiftKey = int(input("Enter your shift key: "))

for letter in myWord:
    myLetters.append(letter)
#print(myLetters)

for letter in myLetters:
    ordLetter = ord(letter)
    ordLetters.append(ordLetter)
    z = ordLetter + shiftKey
    ordEncrypted.append(z)
    encryptedLetters.append(chr(z))

#print(ordLetters)
print(ordEncrypted)
#print(encryptedLetters)

encryptedWord = "".join(encryptedLetters)
print("Your encrypted word is", encryptedWord)
