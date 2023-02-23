#!/bin/bash

# 0 = Manzana 1 = Banano 2 = Naranja
frutas=("Manzana" "Banano" "Naranjas")

# Usamos el @ para mostrar o usar todos los valores
echo "Frutas: ${frutas[@]}"

# Mostramos el valor del indice 1
echo "Fruta 1: ${frutas[1]}"

# Agregamos valores al arreglo
frutas+=("Uvas")

# Usamos el @ para mostrar o usar todos los valores
echo "Frutas: ${frutas[@]}"

unset frutas[1]
# Usamos el @ para mostrar o usar todos los valores
echo "Frutas: ${frutas[@]}"

# Iteramos sobre la lista
for fruta in "${frutas[@]}"; do
	echo $fruta
done

