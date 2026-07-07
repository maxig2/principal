def guardar_usuario(nombre:str, contraseña:str):

    archivo = open("usuarios.txt", "a")

    archivo.write(nombre + "," + contraseña + "\n")

    archivo.close()



def verificar_usuario(nombre:str, contraseña:str)->bool:
    """
    Verifica si un usuario y contraseña existen en usuarios.txt

    Retorna:bool True si existe, False si no existe 
    """

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

def es_entero(texto:str)->bool:

    if texto == "":
        return False

    if texto[0] == "-":
        texto = texto[1:]

    if texto == "":
        return False

    for caracter in texto:

        if caracter < "0" or caracter > "9":
            return False

    return True

def solicitar_entero(mensaje: str) -> int:
    """
    Solicita un número entero al usuario
    """

    numero = input(mensaje)

    while es_entero(numero) == False:
        numero = input("Error. Ingrese un número: ")

    return int(numero)

def solicitar_texto(mensaje: str) -> str:
    """
    Solicita un texto no vacío.
    """

    texto = input(mensaje)

    while texto.strip() == "":
        texto = input("Error. No puede estar vacio: ")

    return texto

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

def modificar_fila(tabla:dict, fila:int)->None:
    """
    Modifica todos los datos de una fila de la tabla.
    Retorna: None
    """

    columnas = tabla["columnas"]
    datos = tabla["datos"]

    for i in range(len(columnas)):

        print("Valor actual:", datos[fila][i])

        datos[fila][i] = input(f"Ingrese nuevo {columnas[i]}: ")

def modificar_columna(tabla:dict,columna:int)->None:
    """
    Modifica todos los datos de una columna de la tabla.
    Retorna: None
    """

    columnas = tabla["columnas"]
    datos = tabla["datos"]

    for i in range(len(datos)):

        print("Valor actual:",datos[i][columna])

        datos[i][columna] = input(f"Fila {i} - Nuevo {columnas[columna]}: ")
    

def mostrar_tabla(tabla: dict)->None:
    """
    Muestra una tabla completa
     Retorna: None
    """

    columnas = tabla["columnas"]
    datos = tabla["datos"]

    for i in range(len(columnas)):
        print(columnas[i], end="\t")

    print()

    for i in range(len(datos)):
        for j in range(len(datos[i])):
            print(datos[i][j], end="\t")

        print()

def mostrar_columna(tabla: dict, columna: int)->None:
    """
    Muestra una columna específica de una tabla.
    """

    datos = tabla["datos"]

    for i in range(len(datos)):
        print(datos[i][columna])

def mostrar_fila(tabla: dict, fila: int)->None:
    """
    Muestra una fila específica de una tabla.
    """

    datos = tabla["datos"]

    for i in range(len(datos[fila])):
        print(datos[fila][i], end="\t")

    print()

def filtrar_columna(tabla: dict, columna: int, valor: str)->None:
    """
    Filtra e imprime las filas donde una columna coincide con un valor
    Retorna: None
    """

    datos = tabla["datos"]

    for i in range(len(datos)):
        if datos[i][columna] == valor:
            print(datos[i])

def existe_proyecto(proyectos: list, nombre: str)->bool:
    """
    Verifica si ya existe un proyecto con ese nombre.

    Retorna: bool: True si el proyecto existe, False en caso contrario.
    """

    resultado = False

    for i in range(len(proyectos)):

        if proyectos[i]["nombre"] == nombre:
            resultado = True

    return resultado

def crear_proyecto(nombre:str)->dict:
    """
    Crea un diccionario que representa un proyecto.

    Retorna: dict: proyecto creado
    """

    proyecto = {}

    proyecto["nombre"] = nombre
    proyecto["tablas"] = []

    return proyecto

def guardar_proyecto(nombre:str)->None:
    """
    Guarda el nombre de un proyecto en proyectos.txt

    Retorna:None
    """

    archivo = open("proyectos.txt", "a")

    archivo.write(nombre + "\n")

    archivo.close()

def agregar_proyecto(proyectos:list,proyecto:dict)->None:
    """
    Agrega un proyecto a la lista de proyectos

    Retorna:None
    """
         
    proyectos.append(proyecto)

def cargar_proyectos()->list:
    """
    Carga todos los proyectos almacenados en proyectos.txt

    Retorna: list: lista de proyectos
    """

    proyectos = []

    archivo = open("proyectos.txt", "a")
    archivo.close()

    archivo = open("proyectos.txt","r")

    for linea in archivo:

        nombre = linea.strip()

        proyecto = crear_proyecto(nombre)

        proyectos.append(proyecto)

    archivo.close()

    return proyectos

def mostrar_proyectos(proyectos:list)->None:
    """
    Muestra todos los proyectos disponibles

    Retorna:None
    """
     
    if len(proyectos) == 0:
        print("No hay proyectos.")

    else:
        for i in range(len(proyectos)):
            print(i, "-", proyectos[i]["nombre"])

def guardar_csv(tabla:dict, nombre:str)->None:
    """
    Guarda una tabla en un archivo CSV

    Retorna:None
    """

    columnas = tabla["columnas"]
    datos = tabla["datos"]
     
    archivo = open(nombre, "w")

    # Guardar encabezados
    linea = ""

    for i in range(len(columnas)):

        linea += columnas[i]

        if i < len(columnas) - 1:
            linea += ","

    archivo.write(linea + "\n")

    # Guardar filas
    for i in range(len(datos)):

        linea = ""

        for j in range(len(datos[i])):

            linea += str(datos[i][j])

            if j < len(datos[i]) - 1:
                linea += ","

        archivo.write(linea + "\n")

    archivo.close()

def cargar_csv(nombre:str)->dict:
    """
    Carga una tabla desde un archivo CSV

    Retorna:dict: diccionario con las claves "columnas" y "tabla"
    """

    resultado = {}

    try:
        archivo = open(nombre, "r")
    except FileNotFoundError:
       print("El archivo no existe.")
       return None

    lineas = archivo.readlines()

    archivo.close()

    columnas = lineas[0].strip().split(",")

    datos = []

    for i in range(1, len(lineas)):

        fila = lineas[i].strip().split(",")

        datos.append(fila)

    resultado["columnas"] = columnas
    resultado["datos"] = datos

    return resultado

def existe_tabla(tablas:list, nombre:str)->bool:

    resultado = False

    for tabla in tablas:

        if tabla["nombre"] == nombre:
            resultado = True

    return resultado

def crear_tabla(nombre:str, columnas:list, datos:list)->dict:
    """
    Crea una tabla.

    Retorna: dict
    """

    tabla = {}

    tabla["nombre"] = nombre
    tabla["columnas"] = columnas
    tabla["datos"] = datos

    return tabla

def agregar_tabla(proyecto:dict, tabla:dict)->None:
    """
    Agrega una tabla a un proyecto.

    Retorna: None
    """

    proyecto["tablas"].append(tabla)

def eliminar_tabla(proyecto:dict,indice:int)->None:
    """
    Elimina una tabla de un proyecto.

    Retorna: None
    """

    proyecto["tablas"].pop(indice)

def seleccionar_tabla(tablas:list)->int:
    """
    Muestra las tablas disponibles.

    Retorna:
        índice elegido
    """

    indice = -1

    if len(tablas)==0:

        print("No hay tablas.")

    else:

        for i in range(len(tablas)):

            print(i,"-",tablas[i]["nombre"])

        indice=int(input("Tabla: "))

        while indice < 0 or indice >= len(tablas):

            indice = int(input("Índice inválido. Tabla: "))

    return indice

def agregar_fila(tabla:dict)->None:
    """
    Agrega una fila.

    Retorna: None
    """

    columnas = tabla["columnas"]
    datos = tabla["datos"]

    fila=[]

    for i in range(len(columnas)):

        valor=input(f"{columnas[i]}: ")

        fila.append(valor)

    datos.append(fila)

def agregar_columna(tabla:dict)->None:
    """
    Agrega una columna.

    Retorna: None
    """

    columnas = tabla["columnas"]
    datos = tabla["datos"]

    nombre=input("Nombre de la columna: ")

    columnas.append(nombre)

    for i in range(len(datos)):

        valor=input(f"Fila {i}: ")

        datos[i].append(valor)

def guardar_proyecto_completo(proyecto:dict)->None:

    guardar_tablas(
        proyecto["nombre"],
        proyecto["tablas"]
    )

    for tabla in proyecto["tablas"]:

        nombre_archivo = (
            proyecto["nombre"]
            + "_"
            + tabla["nombre"]
            + ".csv"
        )

        guardar_csv(
            tabla,
            nombre_archivo
        )

def guardar_tablas(nombre_proyecto:str, tablas:list)->None:
    """
    Guarda los nombres de las tablas de un proyecto.

    Retorna: None
    """

    archivo = open(nombre_proyecto + "_tablas.txt", "w")

    for tabla in tablas:
        archivo.write(tabla["nombre"] + "\n")

    archivo.close()

def cargar_tablas(nombre_proyecto:str)->list:
    """
    Carga las tablas de un proyecto.

    Retorna: list
    """

    tablas = []

    nombre_archivo = nombre_proyecto + "_tablas.txt"

    archivo = open(nombre_archivo, "a")
    archivo.close()

    archivo = open(nombre_archivo, "r")

    for linea in archivo:

        nombre_tabla = linea.strip()

        nombre_csv = nombre_proyecto + "_" + nombre_tabla + ".csv"

        datos = cargar_csv(nombre_csv)

        tabla = crear_tabla(
            nombre_tabla,
            datos["columnas"],
            datos["datos"]
        )

        tablas.append(tabla)

    archivo.close()

    return tablas
