n = int(input('Size: '))
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(i + 1, n + 1):
        print(j, end=' ')
    print()