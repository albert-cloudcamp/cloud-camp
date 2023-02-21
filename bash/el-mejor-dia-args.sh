#!/bin/bash

nombre=$1
complemento=$2

usuario=$(whoami)
directorio=$(pwd)
fecha=$(date)

echo "Buenos días $nombre!"
sleep 1

echo "Hoy te ves bien $nombre!"
sleep 1

echo "Tu tines la mejor $complemento que he visto $nombre!"
sleep 1

echo "Tu usuario es $usuario, estas en el directorio $directorio y la fecha es $fecha"
