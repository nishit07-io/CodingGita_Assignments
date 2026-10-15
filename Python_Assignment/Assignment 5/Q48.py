text = input().strip()
half = len(text) // 2
equal = True

for i in range(half):
	if text[i] != text[i + half]:
		equal = False
		break

if equal:
	print("Equal Halves")
else:
	print("Different Halves")
