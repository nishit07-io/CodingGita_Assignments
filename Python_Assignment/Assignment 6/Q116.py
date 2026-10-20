s = input('String: ')
pairs = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            pairs += 1
print(pairs)
