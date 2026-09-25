marks = 82
attendance = 80

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")