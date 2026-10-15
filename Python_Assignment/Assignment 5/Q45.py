text = input()
middle_index = len(text) // 2

for index in range(len(text)):
	if index == middle_index:
		print(text[index])
