number = 583


hundreds_digit = number // 100

ones_digit = (number % 100) % 10

differnce_beetwen_first_and_last_digit = hundreds_digit - ones_digit
print("Difference between first and last digit:", differnce_beetwen_first_and_last_digit)