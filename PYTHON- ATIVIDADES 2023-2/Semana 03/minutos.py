#Escreva um programa que leia uma quantidade de minutos e mostre a
# quantidade de horas e minutos equivalente.


minutos = int(input(""))
horas = minutos // 60
resto_minutos = minutos % 60

print(f'{horas}h{resto_minutos}min')

#10h0min