n = int(input('Size: '))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(n):
        print('*', end='')
    print()