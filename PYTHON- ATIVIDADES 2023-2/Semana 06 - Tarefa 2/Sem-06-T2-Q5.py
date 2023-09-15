# Você sabia que os pinguins usam jaquetas devido ao frio na Antártida?
# Vamos ajudá-los a converter temperaturas! Escreva um programa que leia
# uma temperatura em Celsius e mostre o resultado em Fahrenheit.

# Lembre-se: °F = (°C * (9/5)) + 32

c = float(input('Digite a temperatura em graus ceusios:'))
f = (c * (9/5)) + 32

print(f'Temperatura em Fahrenheit: {f:.2f}')
