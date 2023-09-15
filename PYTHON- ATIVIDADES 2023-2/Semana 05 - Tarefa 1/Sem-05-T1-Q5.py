numero = int(input())

if numero >= 1000 and numero <= 9999:
    numero_invertido = int(str(numero)[::-1])
    print(numero_invertido)
else:
    print("Número inválido. Por favor, digite um número entre 1000 e 9999.")