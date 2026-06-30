def guardar_usuario(nombre:str, contraseña:str):

    archivo = open("usuarios.txt", "a")

    archivo.write(nombre + "," + contraseña + "\n")

    archivo.close()


def verificar_usuario(nombre:str, contraseña:str):

    resultado = False

    archivo = open("usuarios.txt", "a")
    archivo.close()

    archivo = open("usuarios.txt", "r")

    for linea in archivo:

        datos = linea.strip().split(",")

        if datos[0] == nombre and datos[1] == contraseña:
            resultado = True

    archivo.close()

    return resultado

def es_par(x: int) -> bool:
    """
    Determina si un número es par utilizando recursividad.

    Retorna:
        bool: True si el número es par, False si es impar
    """

    resultado = False

    # Normaliza el número a positivo
    if x < 0:
        x = -x

    # Caso base: 0 es par
    if x == 0:
        resultado = True

    # Caso base: 1 no es par
    elif x == 1:
        resultado = False

    # Paso recursivo
    else:
        resultado = es_par(x - 2)

    return resultado

def es_primo(numero: int, divisor: int = 2) -> bool:
    """
    Determina si un número es primo utilizando recursividad.

    Retorna:
        bool: True si el número es primo, False si no lo es
    """

    resultado = False

    # Caso base: números menores o iguales a 1 no son primos
    if numero <= 1:
        resultado = False
    # Caso base: si el divisor supera la raíz cuadrada, es primo
    elif divisor > numero ** 0.5:
        resultado = True
    # Caso base: si es divisible, no es primo
    elif numero % divisor == 0:
        resultado = False
    # Paso recursivo
    else:
        resultado = es_primo(numero, divisor + 1)

    return resultado
def validar_rango(numero: int, minimo: int, maximo: int) -> bool:
    """
    Verifica si un número se encuentra dentro de un rango.
    Retorna:
        bool: True si el número está dentro del rango, False en caso contrario
    """

    resultado = False

    if numero >= minimo and numero <= maximo:
        resultado = True

    return resultado

def es_multiplo(x: int, multiplo: int) -> bool:
    """
    Determina si un número es múltiplo de otro utilizando recursividad.
    Retorna: bool: True si x es múltiplo de multiplo, False si no
    """

    resultado = False

    # Normaliza a positivo
    if x < 0:
        x = -x

    # Caso base: exacto
    if x == 0:
        resultado = True
    # Caso base: no divisible
    elif x < multiplo:
        resultado = False
    # Paso recursivo
    else:
        resultado = es_multiplo(x - multiplo, multiplo)

    return resultado

def modificar_fila(tabla:list, columnas:list, fila:int)->None:
    """
    Modifica todos los datos de una fila de la tabla.
    Retorna: None
    """

    for i in range(len(columnas)):

        print("Valor actual:", tabla[fila][i])

        nuevo = input(f"Ingrese nuevo {columnas[i]}: ")

        tabla[fila][i] = nuevo

def modificar_columna(tabla:list,columnas:list,columna:int)->None:
    """
    Modifica todos los datos de una columna de la tabla.
    Retorna: None
    """

    for i in range(len(tabla)):

        print("Valor actual:",tabla[i][columna])

        nuevo = input( f"Fila {i} - Nuevo {columnas[columna]}: ")

        tabla[i][columna] = nuevo
    

def mostrar_tabla(tabla: list, columnas: list) -> None:
    """
    Muestra una tabla completa con encabezados.
    """

    for i in range(len(columnas)):
        print(columnas[i], end="\t")

    print()

    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            print(tabla[i][j], end="\t")
        print()

def mostrar_columna(tabla: list, columna: int) -> None:
    """
    Muestra una columna específica de una tabla.
    """

    for i in range(len(tabla)):
        print(tabla[i][columna])

def mostrar_fila(tabla: list, fila: int) -> None:
    """
    Muestra una fila específica de una tabla.
    """

    for i in range(len(tabla[fila])):
        print(tabla[fila][i], end="\t")

    print()

def filtrar_columna(tabla: list, columna: int, valor: str) -> None:
    """
    Filtra e imprime las filas donde una columna coincide con un valor.
    """

    for i in range(len(tabla)):
        if tabla[i][columna] == valor:
            print(tabla[i])

def crear_proyecto(nombre:str,columnas:list,tabla:list)->dict:

    proyecto = {}

    proyecto["nombre"] = nombre
    proyecto["columnas"] = columnas
    proyecto["tabla"] = tabla

    return proyecto

def agregar_proyecto(proyectos:list,proyecto:dict)->None:
        proyectos.append(proyecto)

def mostrar_proyectos(proyectos:list)->None:

    if len(proyectos) == 0:
        print("No hay proyectos.")

    else:
        for i in range(len(proyectos)):
            print(i, "-", proyectos[i]["nombre"])

def guardar_csv(tabla:list, columnas:list, nombre:str)->None:

    archivo = open(nombre, "w")

    # Guardar encabezados
    linea = ""

    for i in range(len(columnas)):

        linea += columnas[i]

        if i < len(columnas) - 1:
            linea += ","

    archivo.write(linea + "\n")

    # Guardar filas
    for i in range(len(tabla)):

        linea = ""

        for j in range(len(tabla[i])):

            linea += str(tabla[i][j])

            if j < len(tabla[i]) - 1:
                linea += ","

        archivo.write(linea + "\n")

    archivo.close()

def cargar_csv(nombre:str)->tuple:

    archivo = open(nombre, "r")

    lineas = archivo.readlines()

    archivo.close()

    columnas = lineas[0].strip().split(",")

    tabla = []

    for i in range(1, len(lineas)):

        fila = lineas[i].strip().split(",")

        tabla.append(fila)

    return columnas, tabla