temperature = float(input("Enter temperature in Celsius: "))

if temperature >= 40:
	print("Very Hot")
elif temperature >= 30:
	print("Hot")
elif temperature >= 20:
	print("Warm")
else:
	print("Cold")
