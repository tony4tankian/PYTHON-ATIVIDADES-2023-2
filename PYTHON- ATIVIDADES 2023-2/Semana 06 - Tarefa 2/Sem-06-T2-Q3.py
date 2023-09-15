# Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas,
# o caixa precisa da sua ajuda para calcular o total! Leia o preço
# de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.

macan = float(input('Digite o valor da maçãn:'))
banana = float(input('Digite o valor da banana:'))

macan = macan * 3
banana = banana * 2

print(f'{macan+banana:1}0')
