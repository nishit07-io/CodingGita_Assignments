text = input('Text: ')
pattern = input('Pattern: ')
for i in range(len(text) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
    if match:
        print(i, end=' ')
print()