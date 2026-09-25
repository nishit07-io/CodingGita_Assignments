order_amount = float(input())
payment_method = input().strip().lower()

if order_amount >= 500:
	if payment_method == "card":
		print("Card Payment Accepted")
	elif payment_method == "upi":
		print("UPI Payment Accepted")
	else:
		print("Unsupported Payment Method")
else:
	print("Minimum Order Amount Not Reached")
