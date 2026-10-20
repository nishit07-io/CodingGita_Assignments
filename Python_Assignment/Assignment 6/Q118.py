s = input('String: ')
for i in range(len(s)):
    first = True
    for k in range(i):
        if s[k] == s[i]:
            first = False
    if first:
        count = 0
        for j in range(len(s)):
            if s[j] == s[i]:
                count += 1
        print(f'{s[i]}: {count}')