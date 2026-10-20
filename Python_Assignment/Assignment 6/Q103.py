s = input('Number: ')
for i in range(len(s)):
    first = True
    for k in range(i):
        if s[k] == s[i]:
            first = False
    count = 0
    for j in range(len(s)):
        if s[j] == s[i]:
            count += 1
    if first and count > 1:
        print(s[i])