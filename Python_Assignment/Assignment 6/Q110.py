groups = int(input('Groups: '))
size = int(input('Numbers per group: '))
for i in range(groups):
    largest = float(input('Number: '))
    for j in range(size - 1):
        x = float(input('Number: '))
        if x > largest:
            largest = x
    print(f'{largest:g}')