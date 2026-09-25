age = int(input())
test_status = input().strip().lower()

if age >= 18:
	if test_status == "pass":
		print("License Approved")
	else:
		print("Test Not Passed")
else:
	print("Age Not Eligible")
