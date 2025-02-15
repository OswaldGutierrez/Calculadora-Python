class ConvertidorNumero:

    def obtenerCaracter(numBuscado):
        tamNum = len(numBuscado)

        for i in range(tamNum):
            if numBuscado[i] == ".":
                print(f"La posición es {i}")
                return i       

    def eliminarCaracter(cadena, posicion):
        primerNum = cadena[:posicion]
        segundoNum = cadena[posicion + 1:]
        return primerNum, segundoNum


    def convertirAFloat(num1, num2):
        numCompleto = float(f"{num1}.{num2}")
        return numCompleto


    if __name__ == '__main__':

        num = "123.45"

        posicionComa = obtenerCaracter(num)
        num2 = eliminarCaracter(num, posicionComa)
        numFloat = convertirAFloat(num2[0], num2[1])
        print(numFloat)
