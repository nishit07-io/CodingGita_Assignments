n = int(input())

for i in range(len(str(n)) - 1):
    n //= 10

print(n)