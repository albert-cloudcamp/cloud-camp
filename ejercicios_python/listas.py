# 0 1 2 3
# -4 -3 -2 -1
# linux = ["Ubuntu", "Amazon Linux", "Debian", "Arch"]

# Accedemos a los valores por medio del indice
# print(linux[1])

# len(linux) # calcular el tamaño de la lista

# También hay índices negativos
#print(linux[-1])

# in es para saber si un elemento se encuentra dentro de la lista
# print("Debian" in linux)

# in busca el valor exacto, funciona como el operador ==
# print("debian" in linux)
# print("Debian" == "debian")

# Preguntamos si un elemento no existe
# print("Mx Linux" not in linux)

# Encontrar el índice de un elemento dentro de la lista
# print(linux.index("Arch"))


# Reemplazar un elemento de nuestra lista
# linux[1] = "Mx Linux"
# print(linux)

# Reemplazar un elemento con otor sin saber el indice
# linux[linux.index("Amazon Linux")] = "Mx Linux"
# print(linux)


# 0 1 2 3
# -4 -3 -2 -1
linux = ["Ubuntu", "Amazon Linux", "Debian", "Arch"]
print(linux)

# Remover un elemento de mi lista
# linux.remove("Arch")
# print(linux)

# Removemos elemento por medio del índice
# linux.pop(1)
# print(linux)

# Agregar un elemento al final de la lista
# linux.append("Mx Linux")

# Agregamos un elemento dependiendo del índice
# linux.insert(1, "Mx Linux")


print(linux)
