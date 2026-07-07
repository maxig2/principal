from paquete.estadisticas import *
from paquete.funciones import *
from paquete.variables import *


proyectos = cargar_proyectos()

proyecto_actual  = -1

#ENTRADAS
nombre = solicitar_texto("ingrese su nombre: ")
contraseña = input("ingrese su contraseña: ")

#PROCESOS
while not verificar_usuario(nombre, contraseña):
    validacion = input("el usuario no esta registrado. ¿desea registrarlo?: ")
    
    while validacion != "si" and validacion != "no":
        validacion = input("ERROR, ingrese 'si' o 'no': ")

    if validacion == "si":

        nombre = input("ingrese el nombre a guardar: ")
        contraseña = input("ingrese la contraseña a guardar: ")
   
        guardar_usuario(nombre,contraseña)

    else:
        nombre = input("ingrese su nombre: ")
        contraseña = input("ingrese su contraseña: ")
          
opcion = ""

while opcion != "f":
    print("Menu de opciones:\na)Proyectos\nb)Tablas\nc)Variables" \
    "\nd)Mostrar\ne)Estadisticas\nf)Salir")

    opcion = input("Seleccione una opcion: ")

    while opcion not in ["a","b","c","d","e","f"]:
        opcion = input("Opción inválida: ")

    match opcion:

        case "a":
            print("1)-crear proyecto:" \
            "\n2)-mostrar proyecto:" \
            "\n3)-seleccionar proyecto:" \
            "\n4)-guardar proyecto:")

            opcion_proyecto = input("opcion: ")

            while opcion_proyecto not in ["1","2","3","4"]:
                opcion_proyecto = input("Opción inválida: ")

            match opcion_proyecto:

                case "1":
                    nombre = solicitar_texto("Nombre del proyecto: ")

                    if existe_proyecto(proyectos, nombre):
                        print("Ese proyecto ya existe.")
                    
                    else:
                        proyecto = crear_proyecto(nombre)

                        agregar_proyecto(proyectos, proyecto)

                        guardar_proyecto(nombre)

                        guardar_tablas(nombre, [])

                        print("Proyecto creado.")

                case "2":
                   mostrar_proyectos(proyectos)

                case "3":
                    mostrar_proyectos(proyectos)

                    indice = solicitar_entero("Proyecto: ")

                    if validar_rango(indice, 0, len(proyectos) - 1):

                        proyecto_actual = indice
                        proyecto = proyectos[proyecto_actual]

                        proyecto["tablas"] = cargar_tablas(proyecto["nombre"])

                        print("Proyecto seleccionado:", proyecto["nombre"])

                    else:
                        print("Proyecto inexistente.")
                
                case "4":
                    if proyecto_actual != -1:
                        proyecto = proyectos[proyecto_actual]

                        guardar_proyecto_completo(proyecto)

                        print("Proyecto guardado.")
                    
                    else:
                        print("Seleccione un proyecto.")
                        
        case "b":

            tablas_menu = input("a)crear/cargar una tabla \n" \
            "b)eliminar tabla \n" \
            "elija una opcion: ")

            while tablas_menu not in ["a", "b"]:
                tablas_menu = input("Opción inválida: ")

            #while tablas_menu != "a" or tablas_menu != "b":
            #    tablas_menu = int("parametro invalido,vuelva a intentar")

            match tablas_menu:

                case "a":

                    if proyecto_actual != -1:

                        nombre_tabla = solicitar_texto("Nombre de la tabla: ")

                        cantidad = solicitar_entero("Cantidad de columnas: ")

                        columnas = []

                        for i in range(cantidad):
                            nombre_columna = solicitar_texto(f"Columna {i+1}: ")

                            columnas.append(nombre_columna)

                        if existe_tabla(proyectos[proyecto_actual]["tablas"], nombre_tabla):
                            print("La tabla ya existe.")
                        else: 
                            tabla = crear_tabla(nombre_tabla, columnas, [])
                            agregar_tabla(proyectos[proyecto_actual], tabla)

                            guardar_proyecto_completo(proyecto)

                            print("Tabla creada.")

                    else:
                        print("Seleccione un proyecto.")
                    
                case "b":
                    if proyecto_actual != -1:

                        proyecto = proyectos[proyecto_actual]

                        indice = seleccionar_tabla(proyecto["tablas"])

                        if indice != -1:

                            eliminar_tabla(proyecto, indice)

                            guardar_proyecto_completo(proyecto)

                            print("Tabla eliminada.")

        case "c":
                if proyecto_actual == -1:
                    print("Seleccione un proyecto.")
        
                else:
                    proyecto = proyectos[proyecto_actual]

                    indice = seleccionar_tabla(proyecto["tablas"])

                    if indice != -1:

                        tabla = proyecto["tablas"][indice]

                        opcion_modificar = input(
                        "1-Modificar fila\n"
                        "2-Modificar columna\n"
                        "3-Agregar fila\n"
                        "4-Agregar columna\n"
                    )
                        
                        while opcion_modificar not in ["1", "2", "3", "4"]:
                            opcion_modificar = input("Opción inválida: ")

                        match opcion_modificar:

                            case "1":

                                fila = solicitar_entero("Fila: ")

                                if validar_rango(fila, 0, len(tabla["datos"]) - 1):
                                    modificar_fila(tabla, fila)
                                    
                                    nombre_archivo = (
                                        proyecto["nombre"] +
                                        "_" +
                                        tabla["nombre"] +
                                        ".csv"
                                )
                                    
                                    guardar_proyecto_completo(proyecto)
                                else:
                                    print("Fila inválida.")

                            case "2":

                                columna = solicitar_entero("Columna: ")

                                if validar_rango(columna, 0, len(tabla["columnas"]) - 1):
                                    modificar_columna(tabla, columna)
                                    
                                    nombre_archivo = (
                                        proyecto["nombre"] +
                                        "_" +
                                        tabla["nombre"] +
                                        ".csv"
                                )
                                    
                                    guardar_proyecto_completo(proyecto)

                                else:
                                    print("Columna inválida.")

                            case "3":
                                agregar_fila(tabla)

                                nombre_archivo = (
                                    proyecto["nombre"] +
                                    "_" +
                                    tabla["nombre"] +
                                    ".csv"
                                )

                                guardar_proyecto_completo(proyecto)
                            
                            case "4":
                                agregar_columna(tabla)

                                nombre_archivo = (
                                    proyecto["nombre"] +
                                    "_" +
                                    tabla["nombre"] +
                                    ".csv"
                                )

                                guardar_proyecto_completo(proyecto)
                     
        case "d":
            if proyecto_actual == -1:
                print("Seleccione un proyecto.")

            else:
                proyecto = proyectos[proyecto_actual]

                indice = seleccionar_tabla(proyecto["tablas"])

                if indice != -1:

                    tabla = proyecto["tablas"][indice]

                    print("--- MOSTRAR ---\n" \
                    "1 - Mostrar tabla completa\n2 - Mostrar fila\n" \
                    "3 - Mostrar columna\n4 - Filtrar por columna")

                    opcion_mostrar = input("Seleccione una opción: ")

                    while opcion_mostrar not in ["1","2","3","4"]:
                        opcion_mostrar = input("Opción inválida: ")

                    match opcion_mostrar:

                        case "1":
                            mostrar_tabla(tabla)

                        case "2":
                            fila = solicitar_entero("Fila: ")

                            if validar_rango(fila, 0, len(tabla["datos"]) - 1):
                                mostrar_fila(tabla, fila)
                            else:
                                print("Fila inválida.")

                        case "3":
                            columna = solicitar_entero("Columna: ")

                            if validar_rango(columna, 0, len(tabla["columnas"]) - 1):
                                mostrar_columna(tabla, columna)
                            else:
                                print("columna inválida.")

                        case "4":
                            columna = solicitar_entero("Columna: ")

                            if validar_rango(columna, 0, len(tabla["columnas"]) - 1):
                                valor = solicitar_texto("Valor: ")

                                filtrar_columna(tabla, columna, valor)
                            
                            else:
                                 print("Columna inválida.")
        case "e":
            if proyecto_actual == -1:
                print("Seleccione un proyecto.")

            else:
                proyecto = proyectos[proyecto_actual]

                indice = seleccionar_tabla(proyecto["tablas"])

                if indice != -1:

                    tabla = proyecto["tablas"][indice]

                    columna = solicitar_entero("Columna: ")

                    if validar_rango(columna, 0, len(tabla["columnas"]) - 1):

                        print(f"""
                        Conteo: {conteo(tabla["datos"])}
                        Máximo: {maximo(tabla["datos"], columna)}
                        Mínimo: {minimo(tabla["datos"], columna)}
                        Promedio: {promedio_aritmetico(tabla["datos"], columna)}
                        Promedio geométrico: {promedio_geometrico(tabla["datos"], columna)}
                        Dispersión: {medidas_dispersion(tabla["datos"], columna)}
                        Mediana: {medidas_posicion(tabla["datos"], columna)}
                        """)

                    else:
                        print("Columna inválida.")
                    
        case "f":
            if proyecto_actual != -1:

                proyecto = proyectos[proyecto_actual]

                for tabla in proyecto["tablas"]:

                    guardar_proyecto_completo(proyecto)

print("Proyecto guardado.")
print("fin del programa") 
