
# Definición de la clase servidor
class Servidor:
    
    _marca = "Dell"
    
    # Este es el constructor y es el que se invoca al momento de la creación de
    # un objeto
    def __init__(self, sistema_operativo, ip):
        self.sistema_operativo = sistema_operativo
        self.ip = ip



# Creación de objetos a partir de la clase
servidor_1 = Servidor("Ubuntu", "10.0.0.23")
servidor_2 = Servidor("Debian", "10.0.0.15")



print(servidor_1.sistema_operativo)

servidor_1.sistema_operativo = "Amazon Linux"
servidor_1._marca = "HP"
print(servidor_1.sistema_operativo)
print(servidor_1._marca)

