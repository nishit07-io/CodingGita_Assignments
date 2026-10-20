n = int(input('Size: '))
for i in range(n // 2):
    for j in range(n):
        if i == 0 and j in (1, n - 2) or (i > 0 and j in (0, n - 1)):
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n // 2):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()