n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        if i in (0, n - 1) or j in (0, n - 1):
            print('1', end='')
        else:
            print('0', end='')
    print()