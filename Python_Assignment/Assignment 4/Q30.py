marks, income = map(int, input().split())

if marks >= 85 or income < 300000:
	print("Scholarship Available")
else:
	print("No Scholarship")
