number = 583

hundreds_digit = number // 100
tens_digit = (number % 100) // 10
ones_digit = (number % 100) % 10

print("Original number:", number)

new_number = ones_digit * 100 + tens_digit * 10 + hundreds_digit
print("New number with digits reversed:", new_number)