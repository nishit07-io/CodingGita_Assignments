number = input("Enter a positive integer: ")
running_sum = 0

for digit in number[::-1]:
	running_sum += int(digit)
	print(running_sum)
