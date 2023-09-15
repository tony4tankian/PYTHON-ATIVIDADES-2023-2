# Solicita ao usuário que digite um caractere
caractere = input("")

# Verifica se o caractere é um símbolo (não é letra ou número)
if not (caractere.isalpha() or caractere.isdigit()) and len(caractere) == 1:
    resultado = True
else:
    resultado = False

# Exibe o resultado
print(resultado)
