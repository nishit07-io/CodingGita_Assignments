marks, attendance = map(int, input().split())

match (marks >= 60, attendance >= 75):
	case (True, True):
		print("Eligible")
	case _:
		print("Not Eligible")
