#VARIABLES

def menu_variables(tablas):

    nombre_tabla  = input("Tabla: ")

    if  nombre_tabla not in tablas:
        print("No existe.")
        return

    fila = []

    for columna in tablas[ nombre_tabla]["columnas"]:

        valor = input(f"{columna}: ")

        fila.append(valor)

    tablas[ nombre_tabla]["filas"].append(fila)

    print("Fila agregada.")
