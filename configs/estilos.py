from tkinter import ttk

color_Fondo = "#202020"
color_Botones_Operaciones = "#323232"
color_Botones_Numeros = "#3b3b3b"
color_Botones_Alternativos = "#76b9ed"
color_Texto = "#ffffff"

# Función para definir y aplicar estilos a los widgets
def aplicar_estilos():

    style = ttk.Style()

    # Estilo de label
    style.configure('styleLabelPrincipal.TLabel', font=("Arial", 40))
    style.configure('styleLabelSecundario.TLabel', font=("Arial", 22))

    # Estilo botones
    style.configure('styleBotonesNumeros.TButton', font=("Arial", 22), width=5, background="#3b3b3b", relief="flat")
    style.configure('styleBotonesOperaciones.TButton', font=("Arial", 22), width=5, background="#323232", relief="flat")
