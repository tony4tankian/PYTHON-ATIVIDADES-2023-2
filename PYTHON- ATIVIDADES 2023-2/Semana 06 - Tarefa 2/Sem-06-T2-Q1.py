# Você sabia que os computadores amam contar coisas?
# Eles são como pequenos nerds! Vamos fazer um contador de letras.
# Peça ao usuário para digitar uma frase qualquer e, em seguida,
# imprima o número de caracteres nessa frase sem considerar espaços
# em branco no início ou final da frase digitada.

frase = input("Digite uma frase qualquer:")
frase = frase.strip(' ')
print('tamanho da frase:',len(frase))


#numero = len(frase)
#i=0
#cont = 0
#while i < numero :
    #print(i,frase[i],ord(frase[i]))
    #i=i+1
    #if ord(frase[i]) != 32:
