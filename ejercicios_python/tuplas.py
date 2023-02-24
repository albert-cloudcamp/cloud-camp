linux = ("Ubuntu", "Amazon Linux", "Debian", "Arch")
print(linux)

# Yo no puedo cambiar los valores de una tupla, esto arroja un error
# linux[1] = "Mx Linux"

# Desestructuración de una tupla en variables individuales
# ubuntu, amazon_linux, debian, arch = linux

ubuntu, amazon_linux, debian = linux
print(debian)
