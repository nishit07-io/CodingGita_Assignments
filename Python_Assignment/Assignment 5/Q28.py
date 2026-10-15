n = int(input("Enter your number: "))
max = 0
for i in range(1 , len(str(n)) + 1):
    digit = n % 10
    if digit > max :
        max = digit
    n = n // 10
print(max)