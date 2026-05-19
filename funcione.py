
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

def Validar_Rangos(valor_minimo: int,
                    valor_maximo: int) -> bool:

    '''
    Solicita al usuario el ingreso de un número
    y verifica si se encuentra dentro de un rango
    determinado utilizando recursividad
    si el número está dentro del rango retorna true
    si el número no está dentro del rango retorna false
    '''

    # Solicita un valor al usuario
    valor_usuario = int(input("Ingrese un valor: "))

    # Verifica si el número está dentro del rango
    if valor_usuario <= valor_maximo and valor_usuario >= valor_minimo:
        return True

    # Si el valor no es válido,
    # la función se vuelve a llamar
    else:
        Recall = Validar_Rangos(0, 10)
        return False


def es_primo(numero, divisor=2):

    '''
    Verifica si un número es primo
    utilizando recursividad
    Retorna bool
     si el número es primo retorna true
     si el número no es primo retorna false
    '''

    # si el números es menor o igual a 1 no es primo
    if numero <= 1:
        return False

    # Si el divisor supera la raíz cuadrada del número es primo
    if divisor > numero ** 0.5:
        return True

    # Si el número es divisible por el divisor no es primo
    if numero % divisor == 0:
        return False

    # La función se vuelve a llamar
    # aumentando el divisor
    return es_primo(numero, divisor + 1)

    # Ejemplos de prueba
print(es_primo(7))   # True
print(es_primo(10))  # False


def validar_rango(numero, minimo, maximo):

    '''
    Verifica si un número se encuentra
    dentro de un rango
    '''

    # Si el número es menor al mínimo,
    # retorna False
    if numero < minimo:
        return False

    # Si el número es mayor al máximo,
    # retorna False
    if numero > maximo:
        return False

    # Si cumple ambas condiciones,
    # retorna True
    return True

    # Ejemplos de prueba
print(validar_rango(5, 1, 10))   # True
print(validar_rango(20, 1, 10))  # False


# Invoca la función
test = Validar_Rangos(0, 10)

# Muestra el resultado
print(test)

def es_multiplo(x: int, multiplo: int) -> bool:
    '''
    verifica si un numero es multiplo de otro utilizando recursividad
    retorna bool
    si es multiplo retorna true
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