n = int(input("Enetr your number: "))
revn = ""
for i in range(1 , len(str(n))  + 1):
    digit = n % 10
    revn = revn + str(digit)
    n = n // 10
print(revn)