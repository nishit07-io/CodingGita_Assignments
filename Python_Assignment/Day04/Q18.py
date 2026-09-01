total_products = 47
products_per_box = 6
complete_boxes = total_products // products_per_box
remaining_products = total_products % products_per_box

print("Number of complete boxes:", complete_boxes)
print("Number of remaining products:", remaining_products)
