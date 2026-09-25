signal = input().strip().lower()

if signal == "red":
	print("Stop")
elif signal == "yellow":
	print("Wait")
elif signal == "green":
	print("Go")
else:
	print("Invalid Signal")
