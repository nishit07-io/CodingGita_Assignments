n = int(input("Enter number: "))
target = int(input("Enter target digit: "))

count = 0

for i in range(len(str(n))):
    digit = n % 10

    if digit == target:
        count += 1

    n = n // 10

print(count)