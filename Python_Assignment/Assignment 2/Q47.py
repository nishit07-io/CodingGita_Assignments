price = "1500"
quantity = "2"
tax_rate = "5"

price = int(price)
quantity = int(quantity)
tax_rate = int(tax_rate)

subtotal = price * quantity
tax_amount = subtotal * (tax_rate / 100)
final_bill = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Price per item:", price)
print("Quantity:", quantity)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)