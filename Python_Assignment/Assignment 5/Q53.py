number = abs(int(input("Enter a number: ")))
largest = 0
second_largest = 0

for _ in range(len(str(number))):
	digit = number % 10
	if digit > largest:
		second_largest = largest
		largest = digit
	elif digit != largest and digit > second_largest:
		second_largest = digit
	number //= 10

if second_largest == 0:
	print("No second largest distinct digit")
else:
	print(second_largest)
