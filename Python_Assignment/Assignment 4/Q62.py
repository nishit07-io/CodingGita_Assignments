price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2000:
    discount_percent = 10
else:
    discount_percent = 0

discount_amount = subtotal * discount_percent / 100
final_amount = subtotal - discount_amount

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_percent}%")
print(f"Final: {final_amount:.2f}")
