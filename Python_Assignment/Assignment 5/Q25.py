n = int(input("Enter your number: "))
count = 1
for i in range(1 , len(str(n)) + 1):
    digit = n % 10
    count = count * digit
    n = n // 10
print(count)