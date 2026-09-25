age, distance = map(int, input().split())

if age < 5:
	print("Free")
elif age >= 60:
	print("Senior")
elif distance <= 10:
	print("Regular - Short Distance")
else:
	print("Regular - Long Distance")
