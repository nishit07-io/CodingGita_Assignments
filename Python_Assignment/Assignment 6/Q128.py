n = int(input('N: '))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(abs(i - j), end=' ')
    print()