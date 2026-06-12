from paquete.estadisticas import *
from paquete.funcione import *
from paquete.variables import *

nombre_guardado = "Emiliano"
contraseña_guardada = 1234

#ENTRADAS
nombre = input("ingrese su nombre: ")
contraseña = input("ingrese su contraseña: ")

#PROCESOS
while nombre != nombre_guardado or contraseña != contraseña_guardada:
    validacion = input("el usuario no esta registrado. ¿desea registrarlo?: ")
    
    while not(validacion == "si" or validacion == "no"):
        validacion = input("ERROR, ingrese 'si' o 'no': ")

    if validacion == "si":

        nombre_guardado = input("ingrese en nombre a guardar: ")
        contraseña_guardada = input("ingrese la contraseña a guardar: ")
    else:
        print("vualva a ingresar el nombre y contraseña") 
        nombre = input("ingrese su nombre: ")
        contraseña = input("ingrese su contraseña: ")
    
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")

menu = print("Menu de opciones:\n(a)Proyectos\n(b)Tablas\n(c)Variables" \
"\n(d)Mostrar\n(e)Estadisticas\n(f)Salir")

opcion = input("Seleccione una opcion: ")
match opcion:
    case "a":
     print("proyectos")
    case "b":
        print("tablas")
    case "c":
        print("hola")
    case "d":
        if len(tabla) == 0:
            print("No hay tablas cargadas.")
        else:
            print("--- MOSTRAR ---")
            print("1 - Mostrar tabla completa")
            print("2 - Mostrar fila")
            print("3 - Mostrar columna")
            print("4 - Filtrar por columna")

            opcion = int(input("Seleccione una opción: "))

            match opcion:

                case 1:
                    mostrar_tabla(tabla, columnas)

                case 2:
                    fila = int(input("Ingrese índice de fila: "))

                    if fila >= 0 and fila < len(tabla):
                        mostrar_fila(tabla, fila)
                    else:
                        print("Fila inválida")

                case 3:
                    columna = int(input("Ingrese índice de columna: "))

                    if columna >= 0 and columna < len(tabla[0]):
                        mostrar_columna(tabla, columna)
                    else:
                        print("Columna inválida")

                case 4:
                    columna = int(input("Ingrese índice de columna: "))
                    valor = input("Ingrese valor a buscar: ")

                    if columna >= 0 and columna < len(tabla[0]):
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

        if columna < 0 or columna >= len(tabla[0]):
            print("Columna inválida")
        else:
            print("Conteo:", conteo(tabla))
            print("Máximo:", maximo(tabla, columna))
            print("Mínimo:", minimo(tabla, columna))
            print("Promedio aritmético:", promedio_aritmetico(tabla, columna))
            print("Promedio geométrico:", promedio_geometrico(tabla, columna))
            print("Medida de dispersión:", medidas_dispersion(tabla, columna))
            print("Mediana:", medidas_posicion(tabla, columna))

    case "f":
        print("fin del programa")