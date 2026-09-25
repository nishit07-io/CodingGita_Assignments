A = int(input("Enter first number"))
B = int(input("Enter second number"))
C = int(input("Eneter third number"))

if A > B:
	if A == C:
		print("A and C both are equal and greatest")
	elif A > C:
		print("A is Greatest")
	else:
		print("C is Greatest")
elif B > A:
	if B == C:
		print("B and C are Equal and Greatest")
	elif B > C:
		print("B is Greatest")
	else:
		print("C is greatest")
else:
	if A > C:
		print("A and B both are greatest")
	elif A == C:
		print("All are equal")
	else:
		print("C is greatest")