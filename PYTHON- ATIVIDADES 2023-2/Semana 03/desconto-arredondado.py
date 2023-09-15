#Escreva um programa de leia o preço de um produto e
# mostre na tela o valor com 10% de desconto arredondado
# para duas casas decimais.


preco =  float(input(""))
deconto = preco * 0.90
preco_com_desconto_arredonddo =  round(deconto,2)

print(preco_com_desconto_arredonddo)