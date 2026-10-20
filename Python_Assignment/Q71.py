n = int(input('Integer: '))
prime = n >= 2
for d in range(2, n):
    if n % d == 0:
        prime = False
print(prime)