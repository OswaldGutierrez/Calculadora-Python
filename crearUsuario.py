from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from configs import estilos
import mysql.connector
import iniciarSesion

usuario = ""
clave = ""

def crearIntefaz():
    global root
    root = Tk()
    root.title("Registro de usuarios")
    root.geometry("255x400")
    framePrincipal = ttk.Frame(root)
    framePrincipal.grid(row=0, column=0)

    global entradaUsuario, entradaClave, validarButton
    entradaUsuario = StringVar()
    entradaClave = StringVar()

    userEntry = ttk.Entry(framePrincipal, textvariable=entradaUsuario)
    userEntry.grid(row=1, column=1)
    userEntry.bind("<KeyRelease>", lambda event: validarDatos())

    claveEntry = ttk.Entry(framePrincipal, textvariable=entradaClave)
    claveEntry.grid(row=1, column=2)
    claveEntry.bind("<KeyRelease>", lambda event: validarDatos())

    validarButton = ttk.Button(framePrincipal, text="Crear usuario", command=lambda: ingresarDatos())
    validarButton.grid(row=2, column=1, columnspan=2)
    validarButton.config(state="disabled")
    root.mainloop()


# Función que se encarga de asignar los valores de usuario y clave a las variables globales. Además, envía esta información a la base de datos.
def ingresarDatos():
    global usuario
    global clave
    global root
    usuario = entradaUsuario.get() 
    clave = entradaClave.get()
    print(f"El usuario es: {usuario}\nLa clave es: {clave}")

    conexion = mysql.connector.connect(user="root", password="root", host="localhost", database="dbcalculadora", port=3306)
    try:
        with conexion:
            with conexion.cursor() as cursor:
                query = "INSERT INTO usuarios(usuario, clave) VALUES (%s, %s)"
                datosUsuarios = (usuario, clave)
                cursor.execute(query, datosUsuarios)
                conexion.commit()
    except mysql.connector.Error as e:
        print(f"Ocurrió un error de tipo:{e}")
    finally:
        conexion.close()
        validarButton.config(state="disabled")
        root.destroy()
        mostrarMensaje("El usuario ha sido creado con éxito")
        iniciarSesion.crearIntefazInicioSesion()
        

# Valida que los entrys no estén vacíos.
def validarDatos():
    if entradaUsuario.get().strip() and entradaClave.get().strip():
        validarButton.config(state="normal")
    else:
        validarButton.config(state="disabled")


def mostrarMensaje(mensaje, titulo="Información"):
    messagebox.showinfo(titulo, mensaje)



if __name__ == "__main__":
    crearIntefaz()

