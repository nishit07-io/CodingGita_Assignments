age = int(input("Enter age: "))

if age < 5:
	print("Free Ticket")
elif age <= 12:
	print("Child Ticket")
elif age <= 59:
	print("Regular Ticket")
else:
	print("Senior Ticket")