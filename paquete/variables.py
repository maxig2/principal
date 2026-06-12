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

def crear_tabla_secuencial():
    tabla = []
    
    print("cargar datos de la tabla.")
    filas = int(input("¿Cuántas filas quieres? "))
    
    for i in range(filas):
        print(f"\n--- Llenando fila {i+1} ---")
        fila = []
        
        columnas = int(input(f"¿Cuántas columnas quieres en la fila {i+1}? "))
        
        for j in range(columnas):
            dato = input(f"Elemento [{i+1}][{j+1}]: ")
            fila.append(dato)
        
        tabla.append(fila)
    
    return tabla