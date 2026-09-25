year, attendance = map(int, input().split())

if year in (2, 3, 4):
	if attendance >= 75:
		print("Room Eligible")
	else:
		print("Attendance Too Low")
else:
	print("Not Eligible by Year")
