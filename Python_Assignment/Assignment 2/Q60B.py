price = "1250"
quantity = "4"
discount = "10"

# Convert string values to appropriate types
price = float(price)
quantity = int(quantity)
discount = float(discount)

# Calculate subtotal
subtotal = price * quantity

# Calculate discount amount
discount_amount = subtotal * (discount / 100)

# Calculate final amount
final_amount = subtotal - discount_amount

# Display results
print("Subtotal: ", subtotal)
print("Discount amount: ", discount_amount)
print("Final amount: ", final_amount)
