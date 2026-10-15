n = int(input("Enter ending number: "))
count = 0
for i in range(1 , n + 1):
    if n % 15 == 0:
        count = count + 1
print(count)