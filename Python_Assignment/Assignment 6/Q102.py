s = input('Number: ')
diff = int(input('D: '))
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if abs(int(s[i]) - int(s[j])) == diff:
            print(s[i], s[j])
