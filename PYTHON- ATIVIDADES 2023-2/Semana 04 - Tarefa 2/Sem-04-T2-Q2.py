# Escreva um programa que leia a idade de uma pessoa
# expressa em anos, meses e dias e
# mostra na tela a idade dessa pessoa
# expressa apenas em dias. Considerar
# sempre os anos com 365 dias e os messes com 30 dias.

anos = int(input())
meses = int(input())
dias = int(input())

anos = anos * 365
meses = meses * 30

total = anos + meses + dias

print(total)