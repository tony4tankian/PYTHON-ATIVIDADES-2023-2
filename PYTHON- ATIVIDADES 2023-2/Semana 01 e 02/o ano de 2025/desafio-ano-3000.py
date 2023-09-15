#Desafio: O ano  3000

# seu programa até agora sóp diz ás pessoas quantos anos elas terão no ano 2025
# e se algum quiser saber quantos anos terá  no ano 2050? ou no ano 300?
#Adicione outra variavel no seu programa,  de modo que o usuario consiga saber
# quantos anos ele terá em  qualquer ano que ele quiser escolher.

nascimento =  int(input("em que ano voçê nasceu ?"))
ano = int(input("Para qual ano voçe quer saber sua idade?"))
idade = ano - nascimento
print("no ano",ano," voçê terar ",idade,"anos!")
