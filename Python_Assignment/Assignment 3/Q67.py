date = input("Enter a date (DD-MM-YYYY): ")

day, month, year = date.split("-")

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(date[-4:])