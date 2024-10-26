class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
      return (
          f"ID: {self.id}, Name: {self.name}, "
          f"Price: {self.price}, Quantity: {self.quantity}"
      )
