
# Funcion con 1 valor de entrada y que retorna un valor al ejecutarse
def hola_mundo(idioma):
    
    if idioma == "es":
        return "Hola mundo".upper()
    
    elif idioma == "en":
        return "Hello world".upper()

# Funciones con multiples valores de entrada
def felicidades(nombre ="Albert", edad ="20"):
    print("Hola " + nombre + " feliz cumpleaños número " + edad)

# Invocación de función con parámetros nombrados
# felicidades(edad="29", nombre="Albert")

felicidades("Lina", "45")
