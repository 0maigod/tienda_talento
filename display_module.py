import gradio as gr
from user_manager import UserManager
from stock_manager import StockManager

class MainLayout:
    def __init__(self):
        self.layout = gr.Blocks()
        self.title = gr.Markdown("# <center>Login/Registro</center>")
        self.stock_file = 'storage/stock.json'
        self.stock_display = gr.Markdown(visible=False)

    def add_title(self, title):
        with self.layout:
            self.title

    def get_layout(self):
            gr.HTML(""" <style> .center-group { 
                                            display: flex; 
                                            justify-content: center; 
                                            align-items: center; 
                                            text-align: center; } 
                            table { 
                                    width: 100%; 
                                    border-collapse: collapse; 
                                    margin: 25px 0; } 
                            th, td { 
                                    padding: 12px; 
                                    text-align: center; 
                                    border: 1px solid #ddd; } 
                            tr:nth-child(even) { background-color: #f2f2f2; } 
                            tr:nth-child(odd) { background-color: #ffffff; } 
                    </style> """)
            with gr.Row("Acceso") as acc:
                with gr.Column():
                    usr = gr.Textbox(placeholder="Username", label="Username")
                    pwd = gr.Textbox(placeholder="Password", type="password", label="Password")
                    btn = gr.Button("Login")
                    out = gr.Label("")

                with gr.Column():
                    reg_usr = gr.Textbox(placeholder="Username", label="Username")
                    reg_pwd = gr.Textbox(placeholder="Password", type="password", label="Password")
                    reg_btn = gr.Button("Register")
                    reg_out = gr.Textbox("")

            with gr.Row():
                self.tabs = gr.Tabs(visible=False)
                with self.tabs: 
                    with gr.Tab("Agregar Producto"):
                        """Muestra el formulario para agregar un producto"""
                        name = gr.Textbox(placeholder="Nombre del producto", label="Nombre")
                        price = gr.Slider(minimum=0, maximum=1000, step=1, label="Precio") # Usamos Slider para el precio 
                        quantity = gr.Slider(minimum=0, maximum=1000, step=1, label="Cantidad") # Usamos Slider para la cantidad
                        add_product_button = gr.Button("Agregar")
                        add_out = gr.Textbox("", label="Resultado de la operación")
                        # self.stock_display = gr.Markdown(visible=False)

                    with gr.Tab("Mostrar Stock"):
                        actualizar_button = gr.Button("Actualizar Stock")
                        self.stock_display = gr.Markdown(self.display_stock())

                    with gr.Tab("Quitar Producto"):
                        self.rem_display = gr.Markdown(self.display_stock())
                        id_to_remove = gr.Slider(minimum=0, maximum=1000, step=1, label="ID del producto a quitar")
                        rem_out = gr.Textbox("", label="Resultado de la operación")
                        remove_button = gr.Button("Quitar Producto")
                        
                    with gr.Tab("Modificar Producto"):
                        modify_button = gr.Button("Modificar Producto") 
                        modify_button.click(fn=self.handle_modify_product)

                    with gr.Tab("Buscar Producto"):
                        modify_button = gr.Button("Buscar Producto") 
                
                actualizar_button.click(fn=self.handle_actualizar_stock,
                            inputs=[],
                            outputs=[self.stock_display])
                
                remove_button.click(fn=self.handle_remove_product,
                            inputs=[id_to_remove],
                            outputs=[self.stock_display, self.rem_display, rem_out, id_to_remove])
            
                add_product_button.click(fn=self.handle_add_product, 
                            inputs=[name, price, quantity], 
                            outputs=[self.stock_display, self.rem_display, name, price, quantity, add_out])
                
                btn.click(fn=self.handle_login, 
                    inputs=[usr, pwd], 
                    outputs=[out, acc, self.tabs, self.title]) 
                
                reg_btn.click(fn=UserManager().register_user,
                            inputs=[reg_usr, reg_pwd],
                            outputs=reg_out)
                
            return self.layout
    
    def handle_login(self, username, password): 
        if UserManager().login_user(username, password): 
            return "Login exitoso", gr.update(visible=False), gr.update(visible=True), gr.update(value="# <center>Inventario</center>")
        else: 
            return "Usuario o contraseña incorrectos", gr.update(visible=True), gr.update(visible=False), gr.update()
    
    def display_stock(self): 
        """Genera una tabla para mostrar el stock actual""" 
        self.stock = StockManager.show_stock()
        stock_table = "| **ID** | **Nombre** | **Precio** | **Cantidad** |\n" 
        stock_table += "|--------|------------|------------|--------------|\n" 
        for product in self.stock: 
            stock_table += f"| {product.id} | {product.name} | {product.price} | {product.quantity} |\n"
        return stock_table
       
    def handle_add_product(self, name, price, quantity): 
        """Maneja la adición de un producto al inventario.""" 
        StockManager.add_product(name, price, quantity) # Llamamos a la función add_product de stock_manager 
        self.stock = StockManager.show_stock()
        return gr.update(value=self.display_stock()), gr.update(value=self.display_stock()), gr.update(value="", visible=True), gr.update(value=0, visible=True), gr.update(value=0, visible=True), gr.update(value="Product added successfully.", visible=True)
        
    def handle_actualizar_stock(self):
        self.stock = StockManager.show_stock()
        print("Actualizando stock...")
        return gr.update(value=self.display_stock())
        
    def handle_remove_product(self, id_to_remove): 
        """Maneja la eliminación de un producto del inventario.""" 
        if StockManager.remove_product(id_to_remove):
            self.stock = StockManager.show_stock()
            return gr.update(value=self.display_stock()), gr.update(value=self.display_stock()), "Product removed successfully.", gr.update(value=0, visible=True)
        else: 
            return gr.update(value=self.display_stock()), gr.update(value=self.display_stock()), "Product not found.", gr.update(value=0, visible=True)

    def handle_modify_product(self): 
        """Maneja la modificación de un producto en el inventario.""" 
        StockManager.modify_product(self.stock) 
        self.tabs[0].children[0].update(self.display_stock())
    