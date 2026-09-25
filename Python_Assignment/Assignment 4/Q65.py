choice = int(input())
quantity = int(input())

match choice:
	case 1:
		price = 250
	case 2:
		price = 150
	case 3:
		price = 200
	case 4:
		price = 120

total = price * quantity
discount = total * 0.10 if total >= 500 else 0
final = total - discount

print(f"Total: {total}, Discount: {discount:.2f}, Final: {final:.2f}")
