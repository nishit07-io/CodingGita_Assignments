a = input('First string: ')
b = input('Second string: ')
for i in range(len(a)):
    first = True
    found = False
    for k in range(i):
        if a[k] == a[i]:
            first = False
    for j in range(len(b)):
        if a[i] == b[j]:
            found = True
    if first and found:
        print(a[i])
