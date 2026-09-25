attendance, marks = map(int, input().split())

if attendance >= 75:
	if marks >= 40:
		print("Pass")
	else:
		print("Fail")
else:
	print("Not Eligible Due to Attendance")
