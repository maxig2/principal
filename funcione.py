
def es_par(x: int) -> bool:
    if x == 0:
        return True
    elif x == 1:
        return False
    else:
        return es_par(x - 2)

resultado = es_par(1)

print(resultado)

def Validar_Rangos (valor_minimo: int, 
                    valor_maximo: int) -> bool:

    '''
    '''
    
    valor_usuario = int(input("ingrese un valor: "))

    if valor_usuario <= valor_maximo and valor_usuario >= valor_minimo:
        return True
    else:
        Recall = Validar_Rangos(0 , 10)
        return False




test = Validar_Rangos(0 , 10)

print(test)
