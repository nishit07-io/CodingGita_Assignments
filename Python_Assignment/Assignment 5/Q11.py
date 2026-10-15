n = int(input("Enter ending number: "))
sum = 0
for i in range(1 , n + 1):
    if i % 3 != 0:
        sum = sum + i
print(sum)