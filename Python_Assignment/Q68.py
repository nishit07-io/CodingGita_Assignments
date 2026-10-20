n = abs(int(input('Integer: ')))
product = 1
for ch in str(n):
    product *= int(ch)
print(product)
