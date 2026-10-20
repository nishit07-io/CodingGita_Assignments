n = int(input('Half-height: '))
w = 2 * n - 1
for i in range(n):
    for j in range(i):
        print(' ', end='')
    width = w - 2 * i
    for j in range(width):
        if j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n - 2, -1, -1):
    for j in range(i):
        print(' ', end='')
    width = w - 2 * i
    for j in range(width):
        if j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()