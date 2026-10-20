a = input('First string: ')
b = input('Second string: ')
count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        count += 1
print(count)