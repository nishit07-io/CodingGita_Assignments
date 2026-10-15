text = input("Enter a string: ")
uppercase = 0
lowercase = 0

for character in text:
	if "A" <= character <= "Z":
		uppercase += 1
	elif "a" <= character <= "z":
		lowercase += 1

print(f"Uppercase = {uppercase}, Lowercase = {lowercase}")
