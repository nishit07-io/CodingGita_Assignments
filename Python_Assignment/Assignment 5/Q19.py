n = int(input("Enter your numbeer: "))
product = 1
for i in range(2 , n + 1 , 2):
    product = product * i
print(product)