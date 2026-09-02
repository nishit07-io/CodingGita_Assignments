number = 5829

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = (number // 1000) % 10

print(ones_digit)
print(tens_digit)
print(hundreds_digit)
print(thousands_digit)
