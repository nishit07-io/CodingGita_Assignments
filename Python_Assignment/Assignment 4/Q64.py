balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
	case 1:
		print(f"Balance: {balance}")
	case 2:
		amount = int(input("Enter deposit amount: "))
		balance += amount
		print(f"Deposit Successful, Balance: {balance}")
	case 3:
		amount = int(input("Enter withdrawal amount: "))
		if amount <= balance:
			balance -= amount
			print(f"Withdrawal Successful, Balance: {balance}")
		else:
			print("Insufficient Balance")
	case 4:
		print("Exiting...")
	case _:
		print("Invalid Choice")
