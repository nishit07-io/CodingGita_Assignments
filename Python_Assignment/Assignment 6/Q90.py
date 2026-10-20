s = input('String: ')
count = 0
for ch in s:
    if ch >= '0' and ch <= '9':
        count += 1
print(count)