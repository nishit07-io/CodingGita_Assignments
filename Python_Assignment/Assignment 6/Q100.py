n = int(input('N: '))
for x in range(2, n + 1):
    prime = True
    for d in range(2, x):
        if x % d == 0:
            prime = False
    if prime:
        print(x, end=' ')
print()