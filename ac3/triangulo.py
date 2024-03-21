def determina_tipo_triangulo(a, b, c ):

    if a + b <= c or a + c <= b or c + b <= a : 
        return "Não é um triangulo "
    
    elif a == b == c :
        return "equilatero"
    
    elif a == b or a == c or b == c :
        return "isoceles "
    
    else: 
        return "escaleno"
    
def testa_triangulo():

    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))

testa_triangulo()       

def dia_semana(numero):
    if numero == 1 : 
        return "domingo"
    elif numero == 2 :
        return "segunda"
    elif numero == 3 : 
        return "terça-feira"
    elif numero == 4 : 
        return "quarta-feira"
    elif numero == 5:
        return "quita-feira"
    elif numero == 6:
        return "sexta-feira"
    elif numero == 7 :
        return "sabado"
    else :
        return "não tem amigo"
    
def testa_dia_semana():
    print(dia_semana(2))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(9))
testa_dia_semana()
