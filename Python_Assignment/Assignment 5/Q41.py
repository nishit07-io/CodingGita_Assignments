
text, target = input().split(",", 1)
text = text.strip()
target = target.strip()

first_index = -1
for index in range(len(text)):
	if text[index] == target:
		first_index = index
		break

if first_index == -1:
	print("Not Found")
else:
	print(first_index)
