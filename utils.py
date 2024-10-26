def validate_price(message):
    while True:
        try:
            price = float(input(message))
            if price <= 0:
                print("Price must be greater than zero.")
            else:
                return price
        except ValueError:
            print("Invalid price. Please enter a number.")

def validate_quantity(message):
    while True:
        try:
            quantity = int(input(message))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                return quantity
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
