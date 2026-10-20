n = int(input('N: '))
for x in range(1, n + 1):
    count = 0
    for d in range(1, x + 1):
        if x % d == 0:
            count += 1
    print(f'{x}: {count}')