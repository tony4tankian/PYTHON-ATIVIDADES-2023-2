preco = float(input())
percentual = float(input())

preco_acrescido = preco + (preco * percentual / 100)
preco_desconto = preco - (preco * percentual / 100)

print(f"{preco_acrescido:.2f}")
print(f"{preco_desconto:.2f}")