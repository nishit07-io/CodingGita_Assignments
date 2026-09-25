account_type, balance = input().split()
balance = float(balance)

if account_type == "savings":
	if balance >= 1000:
		print("Minimum Balance Maintained")
	else:
		print("Minimum Balance Not Maintained")
else:
	print("Unsupported Account")
