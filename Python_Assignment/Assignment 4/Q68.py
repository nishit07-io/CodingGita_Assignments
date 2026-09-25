# Read input
entrance_score = int(input())
percentage_12 = int(input())
category = input().strip().lower()

match category:
    case "general":
        if entrance_score >= 80 and percentage_12 >= 75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "obc":
        if entrance_score >= 70 and percentage_12 >= 70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "sc":
        if entrance_score >= 60 and percentage_12 >= 60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case _:
        print("Admission Not Eligible")
