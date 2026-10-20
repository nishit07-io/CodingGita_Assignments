s = input('String: ')
count = 0
for ch in s:
    if ch.isalpha() and ch.islower():
        count += 1
print(count)