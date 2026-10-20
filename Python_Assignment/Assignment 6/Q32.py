n = int(input('Inner number: '))
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        d = min(i, j, size - 1 - i, size - 1 - j)
        print(n - d, end=' ')
    print()