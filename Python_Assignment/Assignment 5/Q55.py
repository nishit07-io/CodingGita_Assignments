text, target = input().split(",", 1)
text = text.strip()
target = target.strip()

count = 0
for character in text:
	if character == target:
		count += 1

frequency = count / len(text) * 100 if text else 0
frequency_text = f"{frequency:.2f}".rstrip("0").rstrip(".")
if "." not in frequency_text:
	frequency_text += ".0"

print(f"Count = {count}, Frequency = {frequency_text}%")
