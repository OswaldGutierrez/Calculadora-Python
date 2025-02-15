from tkinter import *
from tkinter import ttk
from configs.estilos import aplicar_estilos
from calculos.operaciones import *
from calculos.conversionNum import *



root = Tk()
root.title("CALCULADORA")
root.geometry("+50+200")

framePrincipal = ttk.Frame(root)
framePrincipal.grid(row=0, column=0)


aplicar_estilos()

num1Global = 0
num2Global = 0
signoGlobal = ""

def modificarLabelsNumeros(tecla):
    listaNumeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in listaNumeros:
        if tecla == num:
            entradaPrincipal.set(entradaPrincipal.get() + tecla)

def modificarLabelsOperaciones(tecla):
    global num1Global
    global signoGlobal
    num1Global = float(entradaPrincipal.get())
    listaSignos = ["+", "-", "*", "/"]  

    for signo in listaSignos:
        if tecla == signo:
            signoGlobal = signo
            entradaSecundaria.set(entradaPrincipal.get() + tecla)
            entradaPrincipal.set("")

def realizarOperaciones(tecla):
    global signoGlobal
    global num1Global
    global num2Global
    if tecla == "=":
        num2Global = float(entradaPrincipal.get())
        entradaSecundaria.set(entradaSecundaria.get() + entradaPrincipal.get() + "=")
        if signoGlobal == "+":
            entradaPrincipal.set(Operaciones.opSumar(num1Global, num2Global))
        elif signoGlobal == "-":
            entradaPrincipal.set(Operaciones.opRestar(num1Global, num2Global))
        elif signoGlobal == "*":
            entradaPrincipal.set(Operaciones.opMultiplicar(num1Global, num2Global))
        else:
            entradaPrincipal.set(Operaciones.opDividir(num1Global, num2Global))

def borrarLabels(tecla):
    # El for es innecesario. Como es mi lógica la que estoy mejorando, en vez de quitarlo(opción lógica) lo que hice fue romper el ciclo si la condición se cumple para que el for no siga iterando.
    listaSimbolos = ["CE", "C", "B"]
    for range in listaSimbolos:
        if tecla == "CE":
            entradaPrincipal.set("")    
            break  
        elif tecla == "C":
            entradaPrincipal.set("")
            entradaSecundaria.set("")
            break
        elif tecla == "B":
            if entradaPrincipal.get():
                entradaPrincipal.set(entradaPrincipal.get()[:-1])
                break
        else:
            pass

def operarDecimal():
    numeroActual = entradaPrincipal.get()
    if "." not in numeroActual:
        entradaPrincipal.set(entradaPrincipal.get() + ".")

def convertirNums():
    # Función útil en caso de usar ',' en lugar de '.' para los decimales
    cadenaEntrada = entradaPrincipal.get()
    posicionComa = ConvertidorNumero.obtenerCaracter(cadenaEntrada)
    numsAConvertir = ConvertidorNumero.eliminarCaracter(cadenaEntrada, posicionComa)
    numFloat = ConvertidorNumero.convertirAFloat(numsAConvertir[0], numsAConvertir[1])
    return numFloat



# Etiquetas
entradaSecundaria = StringVar()
labelSecundario = ttk.Label(framePrincipal, textvariable=entradaSecundaria, style='styleLabelSecundario.TLabel')
labelSecundario.grid(row=0, column=3)
entradaPrincipal = StringVar()
labelEntradaPrincipal = ttk.Label(framePrincipal, textvariable=entradaPrincipal, style='styleLabelPrincipal.TLabel')
labelEntradaPrincipal.grid(row=1, column=3)

# Botones
buttonBorrarParcial = ttk.Button(framePrincipal, text="CE", style='styleBotonesOperaciones.TButton', command=lambda: borrarLabels("CE"))
buttonBorrarTodo = ttk.Button(framePrincipal, text="C", style='styleBotonesOperaciones.TButton', command=lambda: borrarLabels("C"))
buttonBorrar = ttk.Button(framePrincipal, text="B", style='styleBotonesOperaciones.TButton', command=lambda: borrarLabels("B"))
buttonComa = ttk.Button(framePrincipal, text=".", style='styleBotonesOperaciones.TButton', command=lambda: operarDecimal())
buttonCalcular = ttk.Button(framePrincipal, text="=", style='styleBotonesOperaciones.TButton', command=lambda: realizarOperaciones("="))
buttonSumar = ttk.Button(framePrincipal, text="+", style='styleBotonesOperaciones.TButton', command=lambda:modificarLabelsOperaciones("+"))
buttonRestar = ttk.Button(framePrincipal, text="-", style='styleBotonesOperaciones.TButton', command=lambda:modificarLabelsOperaciones("-"))
buttonMultiplicar = ttk.Button(framePrincipal, text="*", style='styleBotonesOperaciones.TButton', command=lambda:modificarLabelsOperaciones("*"))
buttonDividir = ttk.Button(framePrincipal, text="/", style='styleBotonesOperaciones.TButton', command=lambda:modificarLabelsOperaciones("/"))
buttonCero = ttk.Button(framePrincipal, text="0", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("0"))
buttonUno = ttk.Button(framePrincipal, text="1", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("1"))
buttonDos = ttk.Button(framePrincipal, text="2", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("2"))
buttonTres = ttk.Button(framePrincipal, text="3", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("3"))
buttonCuatro = ttk.Button(framePrincipal, text="4", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("4"))
buttonCinco = ttk.Button(framePrincipal, text="5", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("5"))
buttonSeis = ttk.Button(framePrincipal, text="6", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("6"))
buttonSiete = ttk.Button(framePrincipal, text="7", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("7"))
buttonOcho = ttk.Button(framePrincipal, text="8", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("8"))
buttonNueve = ttk.Button(framePrincipal, text="9", style="styleBotonesNumeros.TButton", command=lambda: modificarLabelsNumeros("9"))

# Posiciones de los botones
buttonBorrarParcial.grid(row=2, column=0)
buttonBorrarTodo.grid(row=2, column=1)
buttonBorrar.grid(row=2, column=2)
buttonDividir.grid(row=2, column=3)
buttonSiete.grid(row=3, column=0)
buttonOcho.grid(row=3, column=1)
buttonNueve.grid(row=3, column=2)
buttonMultiplicar.grid(row=3, column=3)
buttonCuatro.grid(row=4, column=0)
buttonCinco.grid(row=4, column=1)
buttonSeis.grid(row=4, column=2)
buttonRestar.grid(row=4, column=3)
buttonUno.grid(row=5, column=0)
buttonDos.grid(row=5, column=1)
buttonTres.grid(row=5, column=2)
buttonSumar.grid(row=5, column=3)
buttonComa.grid(row=6, column=0)
buttonCero.grid(row=6, column=1)
buttonCalcular.grid(row=6, column=2, columnspan=2, sticky=("W,E"))

root.mainloop()