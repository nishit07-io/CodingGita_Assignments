age = int(input())
ticket_type = input().strip()

if age < 5:
	print("Free Travel")
elif age >= 60:
	print("Senior Passenger")
elif ticket_type == "AC":
	print("AC Ticket")
elif ticket_type == "Sleeper":
	print("Sleeper Ticket")
else:
	print("Invalid Ticket Type")
