n = int(input("Enter your number: "))
count = 0
for i in range(1 , len(str(n))):
    digit = n % 10
    count = count + 1
    n = n // 10
print(count)