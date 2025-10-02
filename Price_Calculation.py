def calculate_discount(price, discount_percent):
    x = discount_percent
    if x >= 0.2:  # Equivalent to discount of 20%
        final_price = price - price * x
    else:
        final_price = price
    return final_price  # Properly indented inside the function

print(calculate_discount(1000, 0.3))
