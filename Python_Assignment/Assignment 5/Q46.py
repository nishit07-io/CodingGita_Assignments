text = input()
middle = len(text) // 2
first_half = ""
second_half = ""

for index in range(len(text)):
	if index < middle:
		first_half += text[index]
	else:
		second_half += text[index]

print("First Half:", first_half)
print("Second Half:", second_half)
