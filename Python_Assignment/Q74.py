a, b = map(int, input('Enter a and b: ').split())
gcd = 1
for d in range(1, min(a, b) + 1):
    if a % d == 0 and b % d == 0:
        gcd = d
print(gcd)