
# Definición de la clase servidor
class Servidor:
    
    marca = "Dell"
    
    # Este es el constructor y es el que se invoca al momento de la creación de
    # un objeto
    def __init__(self, sistema_operativo, ip):
        self.sistema_operativo = sistema_operativo
        self.ip = ip
        self.programas = []
    
    # Método de instancia
    # Retorna un str con una descripcion del servidor
    def __str__(self):
        return f"El servidor tiene un so: {self.sistema_operativo} y una ip: {self.ip}"

    
    # Método de instancia
    # Que instala programas en el servidor
    def instalar(self, programa):
        self.programas.append(programa)

# Creación de objetos a partir de la clase
servidor_1 = Servidor("Ubuntu", "10.0.0.23")
servidor_2 = Servidor("Debian", "10.0.0.15")


# Instalamos programas dentro del servidor
# servidor_1.instalar("git")
# servidor_1.instalar("htop")

print(servidor_1)
print(servidor_2)
