marks = list(map(float, input().split()))

mark1, mark2, mark3, attendance = marks
total = mark1 + mark2 + mark3
average = total / 3

print(f"Total: {total:g}")
print(f"Average: {average:g}")

if attendance < 75:
	print("Not Eligible")
elif average >= 90:
	print("Outstanding")
elif average >= 75:
	print("Very Good")
elif average >= 60:
	print("Good")
elif average >= 40:
	print("Pass")
else:
	print("Fail")
