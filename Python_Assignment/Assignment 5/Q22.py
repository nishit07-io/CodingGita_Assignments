n = int(input("Enter your number: "))
product = 1
sum = 0
for i in range(1 , n + 1):
    product = product * i
    sum = sum + product
print(sum)