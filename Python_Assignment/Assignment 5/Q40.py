word = input("Enter a word: ")
character = input("Enter a character: ")
count = 0
for i in range(len(word)):
    if word[i] == character:
        count = count + 1
print("The character", character, "appears", count, "times in the word", word)