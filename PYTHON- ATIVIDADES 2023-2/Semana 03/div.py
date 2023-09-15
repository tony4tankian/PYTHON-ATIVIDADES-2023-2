#Escreva um programa que leia dois valores, um dividendo e um divisor.
# Mostre o resultado da divisão e o resto da divisão inteira dos valores.

div = float(input(""))
divs = float(input(""))

inteira = div // divs
resto = div % divs

print(f"{inteira:.4f}")
print(f"{resto:.4f}")