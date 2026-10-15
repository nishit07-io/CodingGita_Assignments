text = input()

symmetric = True
for i in range(len(text) // 2):
	if text[i] != text[-(i + 1)]:
		symmetric = False
		break

if symmetric:
	print("Symmetric")
else:
	print("Not Symmetric")
