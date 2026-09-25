first, second, operator = input().split()
num1 = float(first)
num2 = float(second)

match operator:
	case "+":
		print(num1 + num2)
	case "-":
		print(num1 - num2)
	case "*":
		print(num1 * num2)
	case "/":
		print(num1 / num2)
	case _:
		print("Invalid Operator")
