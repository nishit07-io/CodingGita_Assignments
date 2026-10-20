n = int(input('Size (max 26): '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    print()
for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    print()