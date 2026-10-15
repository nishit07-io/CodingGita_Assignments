n = int(input("Enter your numbeer: "))
product = 1
for i in range(1 , n + 1):
    if n % 2 != 0:
        product = product * i
print(product)