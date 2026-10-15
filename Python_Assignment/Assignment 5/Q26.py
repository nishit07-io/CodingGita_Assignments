n = int(input("Enter your number: "))
count = 0
for i in range(1 , n + 1):
    digit = n % 10
    if digit % 2 == 0:
        count = count + 1
    n = n // 10
print(count)