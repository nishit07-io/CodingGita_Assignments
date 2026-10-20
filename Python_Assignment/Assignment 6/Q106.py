a = input('First string: ')
b = input('Second string: ')
shared = False
for x in a:
    for y in b:
        if x == y:
            shared = True
print(shared)