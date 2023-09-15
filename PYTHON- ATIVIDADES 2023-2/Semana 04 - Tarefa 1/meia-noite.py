#Você gostaria de saber quantos segundos se passaram desde
# a meia-noite? Escreva um programa que leia valores inteiros
# para hora, minuto e segundo. Em seguida, o programa deve calcular e
# imprimir quantos segundos se passaram no total desde a ultima
# meia-noite até a hora lida.


horas = int(input('')) # 1 == 3600 segundos
minutos = int(input('')) # 1 == 60  segundos
segundos = int(input(''))

total_segundos = (horas * 3600) + (minutos * 60) + segundos

print(total_segundos)