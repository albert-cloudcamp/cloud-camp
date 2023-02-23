#!/bin/bash

# Va a controlar cuando el ciclo while va a parar
bandera=true
# Guardar la lista de cosas
cosas=()

while $bandera; do
	echo "Que deseas agregar a tu lista? o presiona s para salir"
	read cosa

	if [[ $cosa != "s" ]]; then
		# Agregamos cosa a la lista de compras
         	cosas+=($cosa)
	else
		bandera=false
	fi

done

echo "Guardando tu lista de compras ......."
sleep 2

echo "${cosas[@]}" > compras.txt

echo "Lista de compras guardada en compras.txt"
