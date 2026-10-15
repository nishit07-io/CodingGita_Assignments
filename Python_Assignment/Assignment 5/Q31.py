n = int(input("Enter number: "))

original = n
reverse = 0

for i in range(len(str(n))):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")