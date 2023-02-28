
# Diccionarios 
# { llave: valor }
inventario = {"Ubuntu": 100, "Amazon Linux": 500, "Debian": 1000, "Arch": 50 }


# Traemos nombre_variable["llave"]
# Si el valor no existe nos arroja una excepción
# print(inventario["debian"])

# Traemos un valor del diccionario, si valor no existe
# retorna None
# print(inventario.get("debian"))

# Cambiamos valores por medio de una llave
# inventario["Debian"] = 34

# Si la llave no existe, agregamos el valor al diccionario
# inventario["Mx Linux"] = 34

# .pop elimina un elemento del diccionario
# inventario.pop("Ubuntu")

# Traemos las llaves de un diccionario
# inventario.keys()

# Traemos todos los valores de un diccionario
# inventario.values()


print(inventario)
