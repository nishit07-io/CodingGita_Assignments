text = input()
swapped = ""

for index in range(0, len(text), 2):
	swapped += text[index + 1] + text[index]

print(swapped)