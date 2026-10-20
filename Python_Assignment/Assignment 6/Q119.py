s = input('String: ')
i = 0
while i < len(s):
    ch = s[i]
    count = 1
    j = i + 1
    while j < len(s) and s[j] == ch:
        count += 1
        j += 1
    if count >= 2:
        print(f'{ch}: {count}')
    i = j