units = int(input())

if units <= 100:
	print("Low Usage")
elif units <= 300:
	print("Medium Usage")
elif units <= 500:
	print("High Usage")
else:
	print("Very High Usage")
