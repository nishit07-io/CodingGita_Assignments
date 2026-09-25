distance = float(input("Enter distance in km: "))
ride_type = input("Enter ride type (normal or premium): ").strip().lower()

match ride_type:
	case "normal":
		fare = distance * 15
	case "premium":
		fare = distance * 25
	case _:
		print("Invalid ride type")
		raise SystemExit

if distance > 20:
	fare *= 1.10

print(f"Fare: {fare:.2f}")
