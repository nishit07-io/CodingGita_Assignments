n = int(input('Even N > 2: '))
for a in range(2, n // 2 + 1):
    b = n - a
    pa = True
    pb = True
    for d in range(2, a):
        if a % d == 0:
            pa = False
    for d in range(2, b):
        if b % d == 0:
            pb = False
    if pa and pb:
        print(a, b)
