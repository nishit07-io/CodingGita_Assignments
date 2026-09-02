number = 9365

thousands_digit = number // 1000
hundreds_digit = (number % 1000) // 100
tens_digit = (number % 100) // 10
ones_digit = number % 10    
print("Thousands digit:", thousands_digit)
print("Hundreds digit:", hundreds_digit)
print("Tens digit:", tens_digit)
print("Ones digit:", ones_digit)