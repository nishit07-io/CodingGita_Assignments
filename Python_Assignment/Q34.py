r = int(input('Rows: '))
c = int(input('Columns: '))
for i in range(r):
    for j in range(c):
        if i in (0, r - 1) or j in (0, c - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
