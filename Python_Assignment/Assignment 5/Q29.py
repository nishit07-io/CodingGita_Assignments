n = int(input("Enter your number: "))
min = 9
for i in range(1 , len(str(n)) + 1):
    digit = n % 10
    if digit < min :
        min = digit
    n = n // 10
print(min)