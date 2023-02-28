
# Estudiantes
# Los definimos como:
# {nombre: "", edad: "", ubicacion: "", correo: ""}
pablo = {"nombre": "Pablo Peralta", "edad": 40, "ubicacion": "Colombia", "correo": "pablo.peralta@mail.com"}
pedro = {"nombre": "Pedro Perez", "edad": 35, "ubicacion": "Perú", "correo": "pedro.perez@mail.com"}


# Profesores
# {nombre: "", edad: "", ubicaciones: "", correo: "", modulos: [""]}
albert = {"nombre": "Albert Ramirez", "edad": 30, "ubicacion": "Colombia", "correo": "albert.ramirez@mail.com", "modulos": ["Bash", "Python"] }


def crear_curso(profesor, lista_estudiantes, tema):
    return {"profesor": profesor, "estudiantes": lista_estudiantes, "tema": tema}

curso = crear_curso(albert, [pablo, pedro], "Bash")

print(curso.get("profesor").get("nombre"))


for estudiante in curso.get("estudiantes"):
    print(estudiante.get("nombre"))
