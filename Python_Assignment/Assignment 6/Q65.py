n = int(input('Size (try 3, 5, 7): '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()