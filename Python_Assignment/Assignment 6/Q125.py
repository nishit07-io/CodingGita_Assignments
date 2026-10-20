n = int(input('Odd N: '))
row_sums = ''
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        value = i + j
        print(value, end=' ')
        total += value
    print() 
    row_sums += str(total) + ' '
    print('Row sums:', row_sums.strip())
    