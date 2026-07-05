#ESTADISTICAS

def validar(datos: list, columna: int) -> bool:
    """
    Verifica si la columna es válida dentro de la tabla.
    """
    resultado = False

    if len(datos) > 0:
        if columna >= 0 and columna < len(datos[0]):
            resultado = True

    return resultado

def conteo(datos: list) -> int:
    """
    Devuelve la cantidad de filas de la tabla.
    """
    resultado = 0

    if len(datos) > 0:
        resultado = len(datos)

    return resultado

def maximo(datos: list, columna: int) -> int:
    """
    Devuelve el valor máximo de una columna.
    """

    resultado = None

    if validar(datos, columna):

        resultado = float(datos[0][columna])

        for i in range(len(datos)):
            valor = float(datos[i][columna])

            if valor > resultado:
                resultado = valor

    return resultado

def minimo(datos: list, columna: int) -> int:
    """
    Devuelve el valor mínimo de una columna.
    """

    resultado = None

    if validar(datos, columna):
        resultado = float(datos[0][columna])

        for i in range(len(datos)):
            valor = float(datos[i][columna])

            if valor < resultado:
                resultado = valor

    return resultado

def promedio_aritmetico(datos: list, columna: int) -> float:
    """
    Calcula el promedio aritmético de una columna.
    """

    resultado = None

    if validar(datos, columna):
        suma = 0

        for i in range(len(datos)):
            suma += float(datos[i][columna])

        resultado = suma / len(datos)

    return resultado

def promedio_geometrico(datos: list, columna: int) -> float:
    """
    Calcula el promedio geométrico de una columna.
    """

    resultado = None

    if validar(datos, columna):
        producto = 1

        for i in range(len(datos)):
            producto *= float(datos[i][columna])

        resultado = producto ** (1 / len(datos))

    return resultado

def medidas_dispersion(datos: list, columna: int):
    """
    Calcula la dispersión (max - min) de una columna.
    """

    resultado = None

    if validar(datos, columna):
        resultado = maximo(datos, columna) - minimo(datos, columna)

    return resultado

def ordenar_burbujas(datos: list) -> list:

    if type(datos) != list:
        print("Debe ser lista.")
        return None

    n = len(datos)

    for i in range(n):

        limite_superior = n - i - 1

        for j in range(limite_superior):

            if datos[j] > datos[j + 1]:

                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux

    return datos

def medidas_posicion(datos: list, columna: int) -> float:
    """
    Calcula la mediana de una columna.
    """

    resultado = None

    if validar(datos, columna):
        valores = []

        for fila in datos:
            valores.append(float(fila[columna]))

        valores = ordenar_burbujas(valores)

        mitad = len(valores) // 2

        if len(valores) % 2 == 0:
            resultado = (valores[mitad - 1] + valores[mitad]) / 2
        else:
            resultado = valores[mitad]

    return resultado