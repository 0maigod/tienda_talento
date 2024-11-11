# from rich.console import Console
# from rich.panel import Panel  # Import the Panel class
# from rich import print  # Import the print function from rich
# from rich.table import Table  # Import the Table class
# from rich.theme import Theme

# def display_items(stock, titulo="List of Products"):
#   """Displays items from the stock manager in an admin interface."""
#   custom_theme = Theme({
#       "info": "dim cyan",
#       "par": "red",
#       "impar": "green",
#   })
#   console = Console(theme=custom_theme)
#   print("\n")
#   if not stock:
#     console.print(Panel("- Stock is empty -", expand=False))
#     return

#   table = Table(title=titulo, show_header=True, show_lines=True, style="bold magenta on black")
#   table.add_column("ID", no_wrap=True)
#   table.add_column("Nombre", no_wrap=True)
#   table.add_column("Precio", no_wrap=True)
#   table.add_column("Cantidad", no_wrap=True)

#   # Definir los estilos para filas alternas
#   alternate_style = True


#   for i, product in enumerate(stock):
#         if alternate_style:
#             row_style = "par"  # Estilo para filas pares
#         else:
#             row_style = "impar"  # Estilo para filas impares

#         table.add_row(
#             str(product.id),
#             product.name,
#             str(product.price),
#             str(product.quantity),
#             style=row_style
#         )

#         alternate_style = not alternate_style
  
#   console.print(table)
#   print(table)

import gradio as gr
from user_manager import UserManager

class LoginLayout:
    def __init__(self):
        self.layout = gr.Blocks()
        self.title = gr.Markdown("# <center>Login/Registro</center>")

    def add_title(self, title):
        with self.layout:
            self.title

    def get_layout(self):
        
        with gr.Row():
            with gr.Accordion("Acceso", open=True) as acc:
                with gr.Row():
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
            tabs = gr.Tabs(visible=False)
                # Pestaña 1: Mostrar Stock with tabs: 
            with tabs:
                with gr.Tab("Mostrar Stock"): 
                    stock_output = gr.Markdown("Aquí se mostrará el stock.") 
                # Pestaña 2: Agregar Producto 
            with tabs:
                with gr.Tab("Agregar Producto"): 
                    agregar_producto_output = gr.Markdown("Aquí se agregarán productos.") 
                # Pestaña 3: Quitar Producto with tabs: 
            with tabs:
                with gr.Tab("Quitar Producto"): 
                    quitar_producto_output = gr.Markdown("Aquí se quitarán productos.") 
                # Pestaña 4: Modificar Producto with tabs: 
            with tabs:
                with gr.Tab("Modificar Producto"): 
                    modificar_producto_output = gr.Markdown("Aquí se modificarán productos.") 
                # Pestaña 5: Buscar Producto with tabs: 
            with tabs:
                with gr.Tab("Buscar Producto"): 
                    buscar_producto_output = gr.Markdown("Aquí se buscarán productos.")
        
            btn.click(fn=self.handle_login, 
                inputs=[usr, pwd], 
                outputs=[out, acc, tabs, self.title]) 
            
            reg_btn.click(fn=UserManager().register_user,
                        inputs=[reg_usr, reg_pwd],
                        outputs=reg_out)
            
        return self.layout
    
    def handle_login(self, username, password): 
        if UserManager().login_user(username, password): 
            return "Login exitoso", gr.update(visible=False), gr.update(visible=True), gr.update(value="# <center>Inventario</center>")
        else: 
            return "Usuario o contraseña incorrectos", gr.update(visible=True), gr.update(visible=False), gr.update()