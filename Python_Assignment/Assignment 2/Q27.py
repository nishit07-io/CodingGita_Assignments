number = 4726

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = (number // 1000) % 10

sum_of_digita = ones_digit + tens_digit + hundreds_digit + thousands_digit
print("Sum of digits:", sum_of_digita)