service_code = int(input())

match service_code:
	case 1:
		print("Check Balance")
	case 2:
		print("Recharge")
	case 3:
		print("Data Usage")
	case 4:
		print("Customer Support")
	case _:
		print("Invalid Service")
