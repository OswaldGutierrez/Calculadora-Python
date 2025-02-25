class Operaciones:
    
    def devolverNumEntero(num):
        if num %1 != 0:
            return num
        else: 
            return int(num)

    def opSumar(num1, num2):
        resultado = num1 + num2
        return Operaciones.devolverNumEntero(resultado)
        

    def opRestar(num1, num2):
        resultado = num1 - num2
        return Operaciones.devolverNumEntero(resultado)

    def opMultiplicar(num1, num2):
        resultado = num1 * num2
        return Operaciones.devolverNumEntero(resultado)

    def opDividir(num1, num2):
        resultado = None
        try:
            resultado = num1/num2
        except ZeroDivisionError as e:
            print(f"Estás intentando dividir por 0. Excepción capturada {e}")
        finally:
            if resultado != None:
                return Operaciones.devolverNumEntero(resultado)
            else: print("Se capturó una excepción")
    

    