s = input('String: ')
result = ''
for ch in s:
    if ch.lower() not in 'aeiou':
        result += ch
print(result)