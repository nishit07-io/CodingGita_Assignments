students = int(input('Students: '))
tests = int(input('Tests: '))
class_total = 0
for i in range(1, students + 1):
    total = 0
    for j in range(1, tests + 1):
        total += int(input(f'Student {i}, test {j}: '))
    print(f'Student {i} total: {total}')
    class_total += total
print('Class total:', class_total)