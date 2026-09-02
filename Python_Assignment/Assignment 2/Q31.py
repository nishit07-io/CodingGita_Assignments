number = 5834

thousands_place = (number // 1000) * 1000
hundreds_place = ((number // 100) % 10) * 100
tens_place = ((number // 10) % 10) * 10
ones_place = number % 10

print("Thousands place:", thousands_place)
print("Hundreds place:", hundreds_place)
print("Tens place:", tens_place)
print("Ones place:", ones_place)    