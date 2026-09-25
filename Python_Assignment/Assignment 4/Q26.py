first, second, operator = input().split()
first = float(first)
second = float(second)

if operator == "+":
	result = first + second
elif operator == "-":
	result = first - second
elif operator == "*":
	result = first * second
elif operator == "/":
	result = first / second
else:
	result = "Invalid Operator"

if result == "Invalid Operator":
	print(result)
elif result.is_integer():
	print(int(result))
else:
	print(result)
