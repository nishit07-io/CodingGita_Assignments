n = int(input('N: '))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        product = i * j
        seen = False
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                if (a < i or (a == i and b < j)) and a * b == product:
                    seen = True
        if not seen:
            print(product, end=' ')
print()
