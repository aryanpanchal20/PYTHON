def calculate_total(price, tax):
    # Calculates the final price with tax
    final_price = price + tax
    return final_price

item_price = 100
tax_amount = "5"  # This is a string, not a number!

# ❌ BROKEN: This will crash the program
print(calculate_total(item_price, tax_amount))
