n = int(input('N: '))
k = int(input('K: '))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        print(f'{i} x {j} = {i * j}')