number = 746

hundreds_digit = number // 100
tens_digit = (number % 100) // 10
ones_digit = (number % 100) % 10

print("Hundreds digit:", hundreds_digit) 
print("The digit in the tens place is:", tens_digit)
print("Ones digit:", ones_digit)