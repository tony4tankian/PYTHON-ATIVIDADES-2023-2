#Escreva um programa que leia uma determinada quantidade de
# minutos e informe essaquantidade
# convertidade para horas e minutos. Por
# exemplo, 220 minutos é equivalente 3 horas e 40 minutos.


minutos = int(input())
segundos = minutos * 60
horas = segundos // 3600
minutos =  minutos %60

print(f'{horas}:{minutos}')
