import mysql.connector

conexion = mysql.connector.connect(user="root", password="root", host="localhost", database="dbcalculadora", port="3306")

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = "INSERT INTO usuarios(usuario, clave) VALUES ('david', '123')"
            cursor.execute(query)
            conexion.commit()
except mysql.connector.Error as e:
    print(f"Ocurrió un error de tipo{e}")
finally:
    conexion.close()
