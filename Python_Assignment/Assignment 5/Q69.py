word = input("Enter a word: ")
count = 0
vc = 0
cc = 0
uc = 0
lc = 0
evencount = 0
for i in word:
    count += 1
    if i in "aeiou":
        vc += 1
    elif i in "bcdfghjklmnpqrstvwxyz":
        cc += 1
    if i == i.isupper():
        uc += 1
    elif i == i.islower():
        lc += 1
    if index % 2 == 0:
        evencount += 1
    index += 1
print("Total number of characters in the word:", count)
print("Total number of vowels in the word:", vc)
print("Total number of consonants in the word:", cc)
print("Total number of uppercase characters in the word:", uc)
print("Total number of lowercase characters in the word:", lc)
print("Total number of even-positioned characters in the word:", evencount)