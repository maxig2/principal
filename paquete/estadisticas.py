#ESTADISTICAS

def validar(tabla: list, columna: int) -> bool:
    """
    Verifica si la columna es válida dentro de la tabla.
    """
    resultado = False

    if len(tabla) > 0:
        if columna >= 0 and columna < len(tabla[0]):
            resultado = True

    return resultado

def conteo(tabla: list) -> int:
    """
    Devuelve la cantidad de filas de la tabla.
    """
    resultado = 0

    if len(tabla) > 0:
        resultado = len(tabla)

    return resultado

def maximo(tabla: list, columna: int) -> int:
    """
    Devuelve el valor máximo de una columna.
    """

    resultado = None

    if validar(tabla, columna):

        resultado = float(tabla[0][columna])

        for i in range(len(tabla)):
            valor = float(tabla[i][columna])

            if valor > resultado:
                resultado = valor

    return resultado

def minimo(tabla: list, columna: int) -> int:
    """
    Devuelve el valor mínimo de una columna.
    """

    resultado = None

    if validar(tabla, columna):
        resultado = float(tabla[0][columna])

        for i in range(len(tabla)):
            valor = float(tabla[i][columna])

            if valor < resultado:
                resultado = valor

    return resultado

def promedio_aritmetico(tabla: list, columna: int) -> float:
    """
    Calcula el promedio aritmético de una columna.
    """

    resultado = None

    if validar(tabla, columna):
        suma = 0

        for i in range(len(tabla)):
            suma += float(tabla[i][columna])

        resultado = suma / len(tabla)

    return resultado

def promedio_geometrico(tabla: list, columna: int) -> float:
    """
    Calcula el promedio geométrico de una columna.
    """

    resultado = None

    if validar(tabla, columna):
        producto = 1

        for i in range(len(tabla)):
            producto *= float(tabla[i][columna])

        resultado = producto ** (1 / len(tabla))

    return resultado

def medidas_dispersion(tabla: list, columna: int):
    """
    Calcula la dispersión (max - min) de una columna.
    """

    resultado = None

    if validar(tabla, columna):
        resultado = maximo(tabla, columna) - minimo(tabla, columna)

    return resultado

def ordenar_burbujas(lista: list) -> list:

    if type(lista) != list:
        print("Debe ser lista.")
        return None

    n = len(lista)

    for i in range(n):

        limite_superior = n - i - 1

        for j in range(limite_superior):

            if lista[j] > lista[j + 1]:

                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista

def medidas_posicion(tabla: list, columna: int) -> float:
    """
    Calcula la mediana de una columna.
    """

    resultado = None

    if validar(tabla, columna):
        valores = []

        for fila in tabla:
            valores.append(float(fila[columna]))

        valores = ordenar_burbujas(valores)

        mitad = len(valores) // 2

        if len(valores) % 2 == 0:
            resultado = (valores[mitad - 1] + valores[mitad]) / 2
        else:
            resultado = valores[mitad]

    return resultado