#VARIABLES

from tablas.tablas import tablas

def menu_variables():

    tabla = input("Tabla: ")

    if tabla not in tablas:
        print("No existe.")
        return

    fila = []

    for columna in tablas[tabla]["columnas"]:

        valor = input(f"{columna}: ")

        fila.append(valor)

    tablas[tabla]["filas"].append(fila)

    print("Fila agregada.")
