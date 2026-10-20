a, b = map(int, input('Enter a and b: ').split())
for x in range(max(a, b), a * b + 1):
    if x % a == 0 and x % b == 0:
        print(x)
        break