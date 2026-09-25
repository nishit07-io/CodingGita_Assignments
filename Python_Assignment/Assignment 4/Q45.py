marks, attendance = map(int, input().split())

if attendance < 75:
	print("Not Eligible")
elif marks >= 90:
	print("Grade A")
elif marks >= 75:
	print("Grade B")
elif marks >= 60:
	print("Grade C")
elif marks >= 40:
	print("Grade D")
else:
	print("Grade F")
