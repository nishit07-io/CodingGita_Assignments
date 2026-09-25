amount, otp = input().split()

if int(amount) <= 50000 and otp == "1234":
	print("Transaction Approved")
else:
	print("Transaction Declined")
