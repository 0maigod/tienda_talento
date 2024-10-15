import display_module
import stock_manager
import search_manager

if __name__ == '__main__':
  stock = stock_manager.load_stock(
    filename='stock.json'
  ) # Load stock from stock.json

  while True:
    print("\nChoose an option:")
    print("1. Display Stock")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Modify Product")  
    print("5. Search Product")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
      display_module.display_items(stock)
    elif choice == '2':
      stock_manager.add_product(stock)
    elif choice == '3':
      stock_manager.remove_product(stock)
    elif choice == '4':
        stock_manager.modify_product(stock)
    elif choice == '5': 
        while True:
            # Display the search submenu
            print("\nSearch by:")
            print("1. Name")
            print("2. Price Range")
            print("3. Low Stock")
            print("4. Back to Main Menu")
      
            search_choice = input("Enter your choice: ")
      
            if search_choice == '1':
              search_manager.search_product(stock)  # Search by name
            elif search_choice == '2':
              # Implement search by price range
              search_manager.search_by_price_range(stock) 
            elif search_choice == '3':
              # Implement search by low stock
              search_manager.search_by_low_stock(stock)
            elif search_choice == '4':
              break  # Go back to the main menu
            else:
              print("Invalid search choice.")
    elif choice == '6':
      break
    else:
      print("Invalid choice.")