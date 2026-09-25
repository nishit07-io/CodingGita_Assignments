units = int(input("Enter units consumed: "))

if units <= 100:
	rate = 5
elif units <= 300:
	rate = 7
else:
	rate = 10

bill = units * rate

print(f"Units: {units}")
print(f"Rate: ₹{rate}")
print(f"Bill: ₹{bill}")
