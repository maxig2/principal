#ESTADISTICAS

from tablas.tablas import tablas

def promedio(lista):

    suma = 0

    for numero in lista:
        suma += numero

    return suma / len(lista)

def maximo(lista):

    mayor = lista[0]

    for numero in lista:

        if numero > mayor:
            mayor = numero

    return mayor

def minimo(lista):

    menor = lista[0]

    for numero in lista:

        if numero < menor:
            menor = numero

    return menor

def menu_estadisticas():

    numeros = []

    cantidad = int(input("Cantidad de numeros: "))

    for i in range(cantidad):

        numero = float(input("Numero: "))
        numeros.append(numero)

    print("Promedio:", promedio(numeros))
    print("Maximo:", maximo(numeros))
    print("Minimo:", minimo(numeros))      
