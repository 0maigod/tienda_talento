from rich.console import Console
from rich.panel import Panel  # Import the Panel class
from rich import print  # Import the print function from rich
from rich.table import Table  # Import the Table class
from rich.theme import Theme

def display_items(stock, titulo="List of Products"):
  """Displays items from the stock manager in an admin interface."""
  custom_theme = Theme({
      "par": "red",
      "impar": "green",
  })
  console = Console(theme=custom_theme)
  print("\n")
  if not stock:
    console.print(Panel("- Stock is empty -", expand=False))
    return

  table = Table(title=titulo, show_header=True, show_lines=True, style="bold magenta on black")
  table.add_column("ID", style="info", no_wrap=True)
  table.add_column("Nombre", style="red", no_wrap=True)
  table.add_column("Precio", style="cyan", no_wrap=True)
  table.add_column("Cantidad", style="cyan", no_wrap=True)

  # Definir los estilos para filas alternas
  alternate_style = True


  for i, product in enumerate(stock):
        if alternate_style:
            row_style = "par"  # Estilo para filas pares
        else:
            row_style = "impar"  # Estilo para filas impares

        table.add_row(
            str(product.id),
            product.name,
            str(product.price),
            str(product.quantity),
            style=row_style
        )

        alternate_style = not alternate_style
  
  console.print(table)
  # print(table)