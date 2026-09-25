salary, rating = map(int, input().split())

if salary >= 30000:
	if rating == 5:
		bonus = 20
	elif rating == 4:
		bonus = 15
	elif rating == 3:
		bonus = 10
	else:
		bonus = 5
	print(f"Bonus: {bonus}%")
else:
	print("Not Eligible for Bonus")
