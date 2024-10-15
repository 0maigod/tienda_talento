import display_module

def search_product(stock):
    """Searches for a product in the stock based on its name."""
    search_term = input("Enter the name of the product to search for: ")
    found_products = []
    for product in stock:
        if search_term.lower() in product.name.lower():
            found_products.append(product)

    if found_products:
        titulo = "Products found in stock"
        display_module.display_items(found_products, titulo)
        # for product in found_products:
        #     print(product)
    else:
        print("No products found matching the search term.")

def search_by_price_range(stock):
    """Searches for products within a specified price range."""
    max_price = float(input("Enter maximum price: "))
    min_price_input = input("Enter minimum price (leave blank for 0): ")

    # Use try-except block to handle potential ValueError
    try:
        min_price = float(min_price_input)
    except ValueError:
        min_price = 0.0

    found_products = [
        product for product in stock
        if min_price <= product.price <= max_price
    ]
    if found_products:
        titulo = "Products found within the price range"
        display_module.display_items(found_products, titulo)
    else:
        print("No products found within the specified price range.")

def search_by_low_stock(stock):
    """Searches for products with low stock (quantity below a threshold)."""
    low_stock_threshold = int(input("Enter the low stock threshold: "))
    found_products = [
        product for product in stock
        if product.quantity < low_stock_threshold
    ]
    if found_products:
        titulo = "Products with low stock"
        display_module.display_items(found_products, titulo)
        # for product in found_products:
        #     print(product)
    else:
        print(f"No products found with stock below {low_stock_threshold}.")