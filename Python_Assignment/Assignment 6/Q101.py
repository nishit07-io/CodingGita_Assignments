s = input('Number: ')
target = int(input('Target: '))
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if int(s[i]) + int(s[j]) == target:
            print(s[i], s[j])