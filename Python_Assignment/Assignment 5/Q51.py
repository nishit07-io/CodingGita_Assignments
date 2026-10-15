text = input("Enter a string: ")

even_count = 0
odd_count = 0

for index in range(len(text)):
	if index % 2 == 0:
		even_count += 1
	else:
		odd_count += 1

print(f"Even Index = {even_count}, Odd Index = {odd_count}")
