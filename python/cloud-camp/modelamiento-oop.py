
class Usuario:
    def __init__(self, nombre, edad, ubicacion, correo):
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.correo = correo    

    def __str__(self):
        return f"Usuario con nombre: {self.nombre} ubicado en {self.ubicacion} y con correo {self.correo}"
    

class Estudiante(Usuario):
    
    def __init__(self, nombre, edad, ubicacion, correo, whatsapp):
        self.whatsapp = whatsapp
        super().__init__(nombre, edad, ubicacion, correo)
   

class Profesor(Usuario):

    def set_modulos(self, modulos):
        self.modulos = modulos


class Curso:
    
    def __init__(self, nombre, profesor, lista_estudiantes):
        self.nombre = nombre
        self.profesor = profesor
        self.lista_estudiantes = lista_estudiantes

    def __str__(self):
        return f"El curso {self.nombre} con el profesor {self.profesor.nombre} tiene {len(self.lista_estudiantes)} estudiantes. "

    def add_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)

pablo = Estudiante("Pablo Peralta", 40, "Colombia", "pablo.peralta@mail.com", "312121212")
pedro = Estudiante("Pedro Perez", 35, "Perú", "pedro.perez@mail.com", "312121212")

albert = Profesor("Albert Ramirez", 30, "Colombia", "albert.ramirez@mail.com")
albert.set_modulos(["Bash", "Python"])
print(albert.modulos)

curso_python = Curso("Introducción a Python", albert, [pablo, pedro])
print(curso_python)

lina =  Estudiante("Lina Perez", 35, "Perú", "lina.perez@mail.com", "312121212")
curso_python.add_estudiante(lina)
print(curso_python)
