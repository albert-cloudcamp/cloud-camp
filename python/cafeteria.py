#!/usr/bin/python3

print("Hola, bienvenido a la cafeteria.")
nombre = input("Cual es tu nombre? \n")


menu = "Cafe, te y agua"
orden = input("Hola, " + nombre + " que desea ordenar de nuestro menu? \n" + menu + "\n")


precio = 4
unidades = int(input("Cuantas unidades deseas? \n"))

max_unidades = 100

if unidades > max_unidades:
    print("Lo lamentamos, pero solamente tenemos " + str(max_unidades) + " unidades de " + orden)
else:
    print("El valor total de tu orden son: " + str(precio * unidades) + " USD")
    print(nombre + " tu " + orden + " estara en un momento. ")
