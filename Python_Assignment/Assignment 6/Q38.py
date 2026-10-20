n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        if i == n or j == 0 or j == 2 * i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()