n = int(input('Count: '))
zeros = 0
for i in range(n):
    if int(input('Number: ')) == 0:
        zeros += 1
print(zeros)