nombre_guardado = "Emiliano"
contraseña_guardada = 1234

#ENTRADAS
nombre = input("ingrese su nombre: ")
contraseña = input("ingrese su contraseña: ")

#PROCESOS
while nombre != nombre_guardado and contraseña != contraseña_guardada:
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
        print("hola")
    case "e":
        suma = 0
        contador = 0
        producto = 1
        primero = True
        seguir = "si"

#arreglar while
        while seguir == "si":
            
            num = int(input("Ingrese un número: "))
            
            if primero == True:
                    maximo = num
                    minimo = num
                    primero = False
            else:
                if num > maximo:
                    maximo = num
                if num < minimo:
                    minimo = num
            producto *= num
            suma += num
            contador += 1
            seguir = input("¿Desea ingresar otro número? (si/no): ")
        
        promedio_aritmetico = suma / contador
        promedio_geometrico = producto ** (1/contador)
        

        print(
    f"La suma es: {suma}\n"
    f"El promedio aritmetico es: {promedio_aritmetico}\n"
    f"El promedio geometrico es: {promedio_geometrico}\n"
    f"El conteo es: {contador}\n"
    f"El maximo es: {maximo}\n"
    f"El minimo es: {minimo}"
)
    case "f":
        print("fin del programa")