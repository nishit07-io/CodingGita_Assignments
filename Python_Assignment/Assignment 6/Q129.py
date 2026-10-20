s = input('Number: ')
count = 0
for i in range(1, len(s) - 1):
    if s[i] > s[i - 1] and s[i] > s[i + 1]:
        count += 1
print(count)