#Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à
#vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar
#em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos
#com até duas casas decimais:

#Valor para pagamento à vista, com desconto de 9%.
#Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
#Valor da prestação para pagamento em 10 vezes, com 17% de juros.


preco = float(input('Digite o um valor:'))

a_vista = preco * 0.91
prestacao_5 = preco / 5
prestacao_10 =  (preco * 1.17) / 10

print(f'{a_vista:.2f}')

print(f'{prestacao_5:.2f}')

print(f'{prestacao_10:.2f}')
