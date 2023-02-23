#!/bin/bash

echo "Hola, que nombre le quieres poner a tu carpeta?"
read nombre_carpeta

echo "Creando carpeta: $nombre_carpeta ......."
rm -rf $nombre_carpeta
mkdir $nombre_carpeta
sleep 2

mensaje="creando archivos"
for i in {1..10}; do
	date > "$nombre_carpeta/archivo_$i"
	sleep 1
	mensaje="$mensaje."
	echo $mensaje
done

echo "Los archivos creados fueron: "
ls $nombre_carpeta
cat $nombre_carpeta/archivo_1
cat $nombre_carpeta/archivo_10
