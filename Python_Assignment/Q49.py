n = int(input('Odd size: '))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i or i == n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()