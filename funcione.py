
def es_par(x: int) -> bool:
    '''
    verifica si un numero es par utilizando recursividad
    retorna bool
    si es par de retorna true
    si no es par retorna false
    '''
#  si el numero llega a 0 es par
    if x == 0:
        return True
# si el numero llega a 1 no es par
    elif x == 1:
        return False
# la funcion se vuelve a llamar restandole 2 al numero
    else:
        return es_par(x - 2)

# invoca la funcion
resultado = es_par(1)

#muestra el resultado
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

def es_multiplo(x: int, multiplo: int) -> bool:
    '''
    verifica si un numero es multiplo de otro utilizando recursividad
    retorna bool
    si es multiplo de retorna true
    si no es multiplo retorna false
    '''
# si el numero llega a 0 es multiplo
    if x == 0:
        return True
# si el numero es negativo no es multiplo   
    elif x < 0:
        return False
# la funcion se vuelve a llamar restandole el multiplo    
    else:
        return es_multiplo(x - multiplo,  multiplo)
    
# invoca la funcion
test = es_multiplo(10, 5)

#muestra el resultado
print(test)