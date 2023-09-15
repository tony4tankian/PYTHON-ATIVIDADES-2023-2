#Escreva um programa que leia um valor inteiro e mostra na tela
# no valor booleano True caso o número lido
# seja maior que 100 ou False caso contrário.

num = int(input())

if num > 100:
    num = True
else:
    num = False

print(num)