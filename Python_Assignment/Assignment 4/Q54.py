grade = input("Enter grade: ").strip().upper()

match grade:
	case "A":
		print("Excellent Performance")
	case "B":
		print("Very Good Performance")
	case "C":
		print("Good Performance")
	case "D":
		print("Needs Improvement")
	case "F":
		print("Failed")
	case _:
		print("Invalid Grade")
