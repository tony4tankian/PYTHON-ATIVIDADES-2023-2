#Escreva um programa/algoritmo que leia 5 (cinco)
# números inteiros e escreva na tela:

#o maior número lido;
#o menor número lido;
#a média aritmética dos números lidos.


num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
num3 = int(input("Digite o terceiro numero:"))
num4 = int(input("Digite o quarto numero:"))
num5 = int(input("Digite o quinto numero:"))

maior =0
if maior < num1:
    maior = num1
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
if maior < num4 :
    maior =  num4
if maior < num5:
    maior = num5

menor =999
if menor > num1:
    menor = num1
if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
if menor > num4 :
    menor =  num4
if menor > num5:
    menor = num5

media = (num1 + num2 + num3 + num4 + num5) / 5


print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {media}')

