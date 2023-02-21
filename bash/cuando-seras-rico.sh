#!/bin/bash

echo "$nombre"

echo "Cual es tu edad?"
read edad

echo "Hola, $nombre tu edad es $edad"

aleatorio=$(( $RANDOM % 21 ))
echo "Hola, $nombre tu edad es $edad y seras rico a los $((edad + aleatorio ))"
