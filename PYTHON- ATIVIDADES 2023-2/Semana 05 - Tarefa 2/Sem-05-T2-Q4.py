# Escreva um programa que leia um caractere e mostra o
# valor booleano True (verdadeiro) se for uma letra (vogal ou consoante)
# ou um dígito (entre ‘0’ e ‘9’) ou
# valor booleano False (falso) caso contrário.




# Solicita ao usuário que digite um caractere
caractere = input("")

# Verifica se o caractere é uma letra (vogal ou consoante) ou um dígito
if (caractere.isalpha() and len(caractere) == 1) or (caractere.isdigit() and len(caractere) == 1):
    resultado = True
else:
    resultado = False

# Exibe o resultado
print(resultado)
