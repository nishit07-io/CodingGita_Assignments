text = input()
length = len(text)
first_half = ""
middle = ""
second_half = ""
half = length // 2

for index, character in enumerate(text):
	if index < half:
		first_half += character
	elif length % 2 == 1 and index == half:
		middle = character
	else:
		second_half += character

print("First Half:", first_half)
if length % 2 == 1:
	print("Middle:", middle)
print("Second Half:", second_half)
