#!/bin/bash
echo "Ingrese el link:"
read LINK
IMAGENES=$(curl "$LINK" | grep "img1" | cut -d '"' -f6 | awk '/.jpg/ { print }')
TOTAL=$(echo "$IMAGENES" | wc -l)
NUM=0
echo "Total de imagenes a bajar: $TOTAL"
sleep 2
for i in $IMAGENES
do
    wget -U Mozilla -O $NUM.jpg $i
    NUM=$(expr $NUM + 1)
done