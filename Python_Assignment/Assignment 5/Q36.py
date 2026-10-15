n = int(input("Enter your number: "))
sum = 0
for i in range(1 , len(str(n)) + 1):
    digit = n % 10
    sum = sum + digit**len(str(n))
    n = n // 10