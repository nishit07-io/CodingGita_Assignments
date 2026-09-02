number = 746

hundreds_digit = number // 100
tens_digit = (number % 100) // 10
ones_digit = (number % 100) % 10

sum_of_digits = hundreds_digit + tens_digit + ones_digit
print("The sum of the digits is:", sum_of_digits)