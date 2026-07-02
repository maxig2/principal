from paquete.estadisticas import *
from paquete.funciones import *
from paquete.variables import *

tabla = []
columnas = []
proyectos = cargar_proyectos()

proyecto_actual  = -1

#ENTRADAS
nombre = input("ingrese su nombre: ")
contraseña = input("ingrese su contraseña: ")

#PROCESOS
while not verificar_usuario(nombre, contraseña):
    validacion = input("el usuario no esta registrado. ¿desea registrarlo?: ")
    
    while validacion != "si" and validacion != "no":
        validacion = input("ERROR, ingrese 'si' o 'no': ")

    if validacion == "si":

        nombre = input("ingrese el nombre a guardar: ")
        contraseña = input("ingrese la contraseña a guardar: ")

        guardar_usuario(nombre, contraseña)

    else:
        nombre = input("ingrese su nombre: ")
        contraseña = input("ingrese su contraseña: ")
          

opcion = ""

while opcion != "f":
    print("Menu de opciones:\na)Proyectos\nb)Tablas\nc)Variables" \
    "\nd)Mostrar\ne)Estadisticas\nf)Salir")

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "a":
            print("1)-crear proyecto:" \
            "\n2)-mostrar proyecto:" \
            "\n3)-seleccionar proyecto:" \
            "\n4)-guardar proyecto:" \
            "\n5)-cargar proyecto")

            opcion_proyecto = input("opcion: ")

            match opcion_proyecto:

                case "1":
                    nombre = input("Nombre del proyecto: ")

                    proyecto = crear_proyecto(nombre, [], [])

                    agregar_proyecto(proyectos, proyecto)

                    guardar_proyecto(nombre)

                    print("Proyecto creado.")

                case "2":
                   mostrar_proyectos(proyectos)

                case "3":
                    mostrar_proyectos(proyectos)

                    indice = int(input("proyecto: "))

                    if indice >= 0 and indice < len(proyectos):
                        proyecto_actual = indice

                        tabla = proyectos[indice]["tabla"]
                        columnas = proyectos[indice]["columnas"]

                        print("Proyecto seleccionado:",proyectos[indice]["nombre"])

                    else:
                         print(" proyecto inexistente")
                
                case "4":
                    if proyecto_actual != -1:
                        guardar_csv(proyectos[proyecto_actual]["tabla"], proyectos[proyecto_actual]["columnas"],"proyecto.csv")

                        print("Proyecto guardado.")
                    
                    else:
                        print("Seleccione un proyecto.")

                case "5":
                    if proyecto_actual != -1:

                        nombre_archivo = proyectos[proyecto_actual]["nombre"] + ".csv"

                        columnas, tabla = cargar_csv(nombre_archivo)

                        proyectos[proyecto_actual]["tabla"] = tabla
                        proyectos[proyecto_actual]["columnas"] = columnas

                        print("Proyecto cargado.")

                    else:
                            print("Seleccione un proyecto.")

        case "b":

            tablas_menu = input("a)crear/cargar una tabla \n" \
            "b)modificar una tabla \n" \
            "elija una opcion: ")

            #while tablas_menu != "a" or tablas_menu != "b":
            #    tablas_menu = int("parametro invalido,vuelva a intentar")

            match tablas_menu:

                case "a":

                    if proyecto_actual != -1:

                        cantidad = int(input("Cantidad de columnas: "))

                        columnas = []

                        for i in range(cantidad):
                            nombre_columna = input(f"Columna {i+1}: ")
                            columnas.append(nombre_columna)

                        tabla = crear_tabla_secuencial()

                        proyectos[proyecto_actual]["tabla"] = tabla
                        proyectos[proyecto_actual]["columnas"] = columnas

                        print("\nTabla final:")

                        for fila in tabla:
                            print(fila)

                    else:
                        print("Seleccione un proyecto.")
                    
                case "b":
                    print("La modificación se realiza desde el menú Variables.")

        case "c":
                if len(tabla) == 0:
                    print("No hay tabla cargada.")
        
                else:
                    opcion_modificar = input("1-Modificar fila\n" "2-Modificar columna\n")

                    match opcion_modificar:

                        case "1":

                            fila = int( input("Fila: "))

                            if fila >= 0 and fila < len(tabla):
                                modificar_fila(tabla,columnas,fila)
                            else:
                                print("Fila inválida.")

                        case "2":

                            columna = int(input("Columna: "))
                            if columna >= 0 and columna < len(columnas):
                                modificar_columna(tabla,columnas,columna)
                            else:
                                print("Columna inválida.")
                     
        case "d":
            if len(tabla) == 0:
                print("No hay tablas cargadas.")
            else:
                print("--- MOSTRAR ---\n" \
                "1 - Mostrar tabla completa\n2 - Mostrar fila\n" \
                "3 - Mostrar columna\n4 - Filtrar por columna")

                opcion_mostrar = int(input("Seleccione una opción: "))

                match opcion_mostrar:

                    case 1:
                        mostrar_tabla(tabla, columnas)

                    case 2:
                        fila = int(input("Fila: "))

                        if fila >= 0 and fila < len(tabla):
                            mostrar_fila(tabla, fila)
                        else:
                            print("Fila inválida")

                    case 3:
                        columna = int(input("Columna: "))

                        if columna >= 0 and columna < len(columnas):
                            mostrar_columna(tabla, columna)
                        else:
                            print("Columna inválida")

                    case 4:
                        columna = int(input("Ingrese índice de columna: "))
                        valor = input("Ingrese valor a buscar: ")

                        if columna >= 0 and columna < len(columnas):
                            filtrar_columna(tabla, columna, valor)
                        else:
                            print("Columna inválida")

                    case _:
                        print("Opción inválida")
        case "e":
            if len(tabla) == 0:
                print("No hay tabla cargada.")

            else:
                columna = int(input("Columna a analizar: "))

                if columna < 0 or columna >= len(columnas):
                    print("Columna inválida")
                else:
                    print(f"""--- ESTADÍSTICAS DE LA COLUMNA ---
            Conteo: {conteo(tabla)}
            Máximo: {maximo(tabla, columna)}
            Mínimo: {minimo(tabla, columna)}
            Promedio aritmético: {promedio_aritmetico(tabla, columna)}
            Promedio geométrico: {promedio_geometrico(tabla, columna)}
            Medida de dispersión: {medidas_dispersion(tabla, columna)}
            Mediana: {medidas_posicion(tabla, columna)}""")
                    
        case "f":
            if proyecto_actual != -1:

               nombre_archivo = proyectos[proyecto_actual]["nombre"] + ".csv"

               guardar_csv(
                     proyectos[proyecto_actual]["tabla"],
                     proyectos[proyecto_actual]["columnas"],
                     nombre_archivo
                )

print("Proyecto guardado.")
print("fin del programa") 
