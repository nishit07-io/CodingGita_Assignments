s = input('String: ')
result = ''
for ch in s:
    if not '0' <= ch <= '9':
        result += ch
print(result)
