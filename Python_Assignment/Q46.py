n = int(input('Rows: '))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        if j < i:
            value = value * (i - j) // (j + 1)
        else:
            value = value
    print()
