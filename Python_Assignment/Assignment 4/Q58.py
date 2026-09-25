student_id = input()
degree, batch, branch, roll_number = student_id.split("-")

if branch == "CSE":
	print("CSE Student")
else:
	print("Non-CSE Student")
