#!/bin/bash

printf "Inicializando...\n\n"

rm -f ./*.jl ./*.json

sleep 2

printf "\n\nSoltando arañas...\n\n"
sleep 2
scrapy crawl obranuevabarcelona -o output.json
sleep 2
printf "\n\nMostrando resultados...\n\n"
sleep 1
./simple_log_reader.py output.json
