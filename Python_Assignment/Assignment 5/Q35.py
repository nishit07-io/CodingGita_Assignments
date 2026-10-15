n = int(input("Enter your number: "))
sum = 0

for i in range(0 , len(str(n))):
    digit = n % 10
    sum = sum + digit**len(str(n))
    n = n // 10
if sum == n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")