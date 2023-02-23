#!/bin/bash

# Ciclo for, lo usamos para iterar sobre valores definidos
for archivo in /home/ec2-user/*; do
	echo $archivo
done


# Ciclo while, lo usamos para iterar sobre una condicion
mensaje="Esperando"
while true; do
	mensaje="$mensaje."
	echo $mensaje
	sleep 1
done

