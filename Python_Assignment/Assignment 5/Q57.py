number = input().strip()

even_count = 0
odd_count = 0

for digit in number:
	if int(digit) % 2 == 0:
		even_count += 1
	else:
		odd_count += 1

if even_count > odd_count:
	print("More Even Digits")
elif odd_count > even_count:
	print("More Odd Digits")
else:
	print("Equal")
