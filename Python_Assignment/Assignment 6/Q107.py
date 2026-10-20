r = int(input('Rows: '))
seats = int(input('Seats per row: '))
for i in range(1, r + 1):
    print(f'Row {i}:', end=' ')
    for j in range(1, seats + 1):
        print(j, end=' ')
    print()