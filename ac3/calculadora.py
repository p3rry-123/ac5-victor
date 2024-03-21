
def calculadora ():

    num1 = float(input("informe um numero") )
    num2 = float(input("informe outro numero") )
    operaçao = input("informe a operaçao ")

    if operaçao == "soma":
        resultado = num1 + num2
        return resultado
    
    elif operaçao == "subtraçao":
        resultado = num1 - num2
        return resultado
    
    elif operaçao == "divisao":
        resultado = num1 / num2
        return resultado
    
    elif operaçao == "multiplicaçao":
        resultado = num1 * num2
        return resultado
    
print(calculadora())