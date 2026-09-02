product_cost = 2000
discount = 15
gst = 18

price_after_discount = product_cost - (product_cost * discount / 100)
total_cost = price_after_discount + (price_after_discount * gst / 100)


print("Price after Discount:", price_after_discount)
print("Total Cost after GST:", total_cost)