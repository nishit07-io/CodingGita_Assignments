n = abs(int(input('Integer: ')))
count = 1
while n >= 10:
    n //= 10
    count += 1
print(count)
