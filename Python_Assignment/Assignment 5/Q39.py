word = input("Enter a word: ").lower()
cv = 0
cc = 0
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cv = cv + 1
    else:
        cc = cc + 1
print("The number of vowels in the word is:", cv)
print("The number of consonants in the word is:", cc)