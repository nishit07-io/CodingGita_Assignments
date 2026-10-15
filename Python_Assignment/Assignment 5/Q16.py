n = int(input("Enter number: "))
product = 1
for i in range(1 , n + 1):
    product = product * i
print(f"{n}! = {product}")