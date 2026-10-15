n = int(input("Enter your number: "))

max = 0
min = 9
for i in range(0 , len(str(n))):
    digit = n % 10
    if digit > max :
        max = digit
    if min > digit:
        min = digit
    n = n // 10
print(max - min)