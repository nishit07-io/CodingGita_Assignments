text = input()

current_count = 0
best_count = 0
previous = None

for character in text:
	if character == previous:
		current_count += 1
	else:
		current_count = 1
		previous = character

	if current_count > best_count:
		best_count = current_count

print(best_count)
