class Operaciones:
    
    def opSumar(num1, num2):
        resultado = num1 + num2
        return resultado

    def opRestar(num1, num2):
        resultado = num1 - num2
        return resultado

    def opMultiplicar(num1, num2):
        resultado = num1 * num2
        return resultado

    def opDividir(num1, num2):
        resultado = None
        try:
            resultado = num1/num2
        except ZeroDivisionError as e:
            print(f"Estás intentando dividir por 0. Excepción capturada {e}")
        finally:
            if resultado != None:
                return resultado
            else: print("Se capturó una excepción")
    

    