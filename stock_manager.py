import display_module
import json
from product import Product
from utils import validate_price, validate_quantity

class StockManager:

    def show_stock():
        """Displays the stock."""
        stock = load_stock()
        return stock

    def modify_product(stock):
        """Modifies an existing product in the stock."""
        titulo = "List of Items"
        display_module.display_items(stock, titulo)
        id_to_modify = int(input("Enter the ID of the product to modify: "))
        
        for i, product in enumerate(stock):
            if product.id == id_to_modify:
                print(f"Current values for product {product.id}:")
                print(f"Name: {product.name}")
                print(f"Price: {product.price}")
                print(f"Quantity: {product.quantity}")
            
                new_name = input("Enter new name (leave blank to keep current): ")
                if new_name:
                    product.name = new_name
            
                new_price = validate_price("Enter new price (leave blank to keep current): ")
                if new_price:
                    product.price = float(new_price)
            
                new_quantity = validate_quantity("Enter new quantity (leave blank to keep current): ")
                if new_quantity:
                    product.quantity = int(new_quantity)
            
                print("Product modified successfully.")
                save_stock(stock)
            return
        
        print("Product not found.")

    

    def add_product(name, price, quantity): 
        """Adds a new product to the stock and updates the stock.json file.""" 
        stock = load_stock()
        id = len(stock) + 1 # Assuming IDs start from 1 
        product = Product(id, name.capitalize(), price, quantity) 
        stock.append(product) # Add the product to the stock list 
        save_stock(stock) # Save the updated stock to stock.json

    def remove_product(id_to_remove):
        """Removes a product from the stock."""
        stock = load_stock()
        product_removed = False  # Bandera para controlar si se ha eliminado el producto
        for i, product in enumerate(stock):
            if product.id == id_to_remove:
                del stock[i]
                product_removed = True  # Producto encontrado y eliminado
                save_stock(stock)  # Guardamos el stock actualizado
                break  # Salimos del bucle una vez que el producto ha sido eliminado
        return product_removed  # Devolvemos True si el producto fue eliminado, False de lo contrario


def save_stock(stock, mode='json'):
        """Saves stock data to a file.
        
        Args:
        stock (list): The list of Product objects.
        mode (str, optional): The saving mode ('json', 'csv'). Defaults to 'json'.
        """
        if mode == 'json':
            with open('storage/stock.json', 'w') as f:
                json.dump([product.__dict__ for product in stock], f, indent=4)
        else:
            print("Invalid saving mode.")

def load_stock(filename=None):  
    """Loads stock data from a json file.
    
    Args:
        filename (str, optional): The filename to load from. Defaults to None.
        mode (str, optional): The loading mode ('json'). 
        Defaults to 'json'.
    
    Returns:
        list: A list of Product objects.
    """
    stock = []

    with open(str('storage/stock.json'), 'r') as f:
        data = json.load(f)  # Load the JSON data

        if isinstance(data, list):  # Check if it's a list of product objects
            stock = [
                Product(
                product['id'], 
                product['name'], 
                product['price'], 
                product['quantity']
                ) 
                for product in data
            ]
        else:  # Assume it's a single product object
            stock = [Product(data['id'], 
                            data['name'], 
                            data['price'], 
                            data['quantity'])]


    return stock