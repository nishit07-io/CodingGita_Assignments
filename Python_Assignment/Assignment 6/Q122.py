n = int(input('N: '))
for x in range(2, n + 1):
    total = 0
    for d in range(1, x):
        if x % d == 0:
            total += d
    if total == x:
        print(x)
