s = input('String: ')
result = ''
for ch in s:
    if ch == 'a':
        result += 'e'
    else:
        result += ch
print(result)