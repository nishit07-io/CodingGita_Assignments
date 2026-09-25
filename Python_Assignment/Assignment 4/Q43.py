plan, usage = input().split()
usage = float(usage)

if plan == "basic":
	if usage > 100:
		print("Recommend Upgrade")
	else:
		print("Basic Plan Is Sufficient")
else:
	print("Already on Higher Plan")
