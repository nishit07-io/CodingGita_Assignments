balance, withdrawal = map(int, input().split())

if withdrawal > balance:
	print("Insufficient Balance")
elif withdrawal % 100 != 0:
	print("Enter Amount in Multiples of 100")
else:
	print("Withdrawal Successful")
