# import math # Importa el módulo completo y se accede a sus constantes, funciones y demás por medio del .

# from math import pi as constante_pi # importamos pi y le cambiamos el nombre

# from math import * # importamos todo desde la módulo math

from mis_modulos.mi_modulo import get_servers

for server in get_servers():
    print(server)

