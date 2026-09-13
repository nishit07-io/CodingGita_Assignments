name = input()
marks = list(map(int, input().split()))

total = sum(marks)
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
