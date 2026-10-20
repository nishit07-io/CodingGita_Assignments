a = input('First string: ')
b = input('Second string: ')
same = len(a) == len(b)
for ch in a:
    ca = 0
    cb = 0
    for x in a:
        if x == ch:
            ca += 1
    for x in b:
        if x == ch:
            cb += 1
    if ca != cb:
        same = False
for ch in b:
    found = False
    for x in a:
        if x == ch:
            found = True
    if not found:
        same = False
print(same)