number = 5836

# Extract individual digits
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10

# Sum of digits
sum_of_digits = ones + tens + hundreds + thousands

# Reversed number
reversed_number = int(str(number)[::-1])

# Display results
print("Number: ", number)
print("Thousands digit: ", thousands)
print("Hundreds digit: ", hundreds)
print("Tens digit: ", tens)
print("Ones digit: ", ones)
print("Sum of digits: ", sum_of_digits)
print("Reversed number: ", reversed_number)
