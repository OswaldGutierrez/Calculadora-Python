from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import abrirCalculadora
import mysql.connector

usuario = ""
clave = ""

def crearIntefazInicioSesion():
    root = Tk()
    root.title("Inicio de Sesión")
    root.geometry("255x400")
    framePrincipal = ttk.Frame(root)
    framePrincipal.grid(row=0, column=0)

    global entradaUsuario, entradaClave, validarButton
    entradaUsuario = StringVar()
    entradaClave = StringVar()

    userEntry = ttk.Entry(framePrincipal, textvariable=entradaUsuario)
    userEntry.grid(row=1, column=1)

    claveEntry = ttk.Entry(framePrincipal, textvariable=entradaClave)
    claveEntry.grid(row=1, column=2)

    validarButton = ttk.Button(framePrincipal, text="INGRESAR", command=lambda: asignarDatos(root))
    validarButton.grid(row=2, column=1, columnspan=2)
    root.mainloop()


def asignarDatos(root):
    global usuario, clave
    usuario = entradaUsuario.get() 
    clave = entradaClave.get()
    print(f"El usuario es: {usuario}\nLa clave es: {clave}")
    conexion = mysql.connector.connect(user="root", password="root", host="localhost", database="dbcalculadora", port="3306")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                query = "SELECT * FROM usuarios WHERE usuario=%s AND clave=%s"
                datosInicioSesion = (usuario, clave)
                cursor.execute(query, datosInicioSesion)
                registroUsuario = cursor.fetchall()
                registrosEncontrados = cursor.rowcount
                print(f"Los datos encontrados son:{registroUsuario}")               

    except mysql.connector.Error as e:
        print(e)
    finally:
        conexion.close()
        if registrosEncontrados != 0:
            root.destroy()
            mostrarMensaje("BIENVENIDO")
            abrirCalculadora()
        else:
             mostrarMensaje("USUARIO O CLAVE INCORRECTO")


    
def mostrarMensaje(mensaje, titulo="Información"):
    messagebox.showinfo(titulo, mensaje)



if __name__ == "__main__":
    crearIntefazInicioSesion()

