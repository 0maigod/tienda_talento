# import display_module
# import stock_manager
# import search_manager
# import user_manager


# if __name__ == '__main__':
#   stock = stock_manager.load_stock(
#     filename='storage/stock.json'
#   ) # Load stock from stock.json

#   users = user_manager.load_users(
#     filename='storage/users.json'
#   ) # Load users from users.json

#   while True:
#     print("\nChoose an option:")
#     print("1. Login")
#     print("2. Register")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#       logged_in = user_manager.login_user()
#       if not logged_in:
#         continue
#     elif choice == '2':
#       logged_in = user_manager.register_user()
#     elif choice == '3':
#       break

#     while logged_in:
#       print("\nChoose an option:")
#       print("1. Display Stock")
#       print("2. Add Product")
#       print("3. Remove Product")
#       print("4. Modify Product")  
#       print("5. Search Product")
#       print("6. Logout")
      
#       choice = input("Enter your choice: ")

#       if choice == '1':
#         display_module.display_items(stock)
#       elif choice == '2':
#         stock_manager.add_product(stock)
#       elif choice == '3':
#         stock_manager.remove_product(stock)
#       elif choice == '4':
#           stock_manager.modify_product(stock)
#       elif choice == '5': 
#           while True:
#               # Display the search submenu
#               print("\nSearch by:")
#               print("1. Name")
#               print("2. Price Range")
#               print("3. Low Stock")
#               print("4. Back to Main Menu")
        
#               search_choice = input("Enter your choice: ")
        
#               if search_choice == '1':
#                 search_manager.search_product(stock)  # Search by name
#               elif search_choice == '2':
#                 # Implement search by price range
#                 search_manager.search_by_price_range(stock) 
#               elif search_choice == '3':
#                 # Implement search by low stock
#                 search_manager.search_by_low_stock(stock)
#               elif search_choice == '4':
#                 break  # Go back to the main menu
#               else:
#                 print("Invalid search choice.")
#       elif choice == '6':
#         logged_in = False
#         break
#       else:
#         print("Invalid choice.")

import gradio as gr
from user_manager import UserManager



with gr.Blocks() as demo:
    gr.Markdown("# Login Screen")
    with gr.Row():
        usr = gr.Textbox(placeholder="Username", label="Username")
        pwd = gr.Textbox(placeholder="Password", type="password", label="Password")
    btn = gr.Button("Login")
    out = gr.Label("")

    btn.click(fn=UserManager().login_user,
              inputs=[usr, pwd],
              outputs=out)

    reg_usr = gr.Textbox(placeholder="Username", label="Username")
    reg_pwd = gr.Textbox(placeholder="Password", type="password", label="Password")
    reg_btn = gr.Button("Register")
    reg_out = gr.Label("")

    reg_btn.click(fn=UserManager().register_user,
                  inputs=[reg_usr, reg_pwd],
                  outputs=reg_out)
 

if __name__ == "__main__":
    demo.launch()
