n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(i):
        if i == n or j == 0 or j == i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
