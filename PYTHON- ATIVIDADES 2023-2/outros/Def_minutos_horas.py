# Define uma função chamada_ minutos_para_horas() e recebe um argumento como parâmetro
def minutos_para_horas(qtd_minutos):
    #Horas recebe  o  valor de qtd_minutos // 60
    horas = qtd_minutos // 60
    #Minutos recebe o valor de qtd_minutos resto da divisao  por 60
    minutos = qtd_minutos % 60
    #Retorna uma string  concatenada os valores de hora e minutos
    return f'{horas}h{minutos}min'

#Minutos recebe digitado do usuário um valor inteiro
minutos = int(input('Quantidade de Minutos:'))
#Horas o valor retornado da função minutos_para_horas() com parametro minutos
horas = minutos_para_horas(minutos)
#Função print() imprime na tela uma estring com valores das variáveis  minutos e horas
print(f'{minutos} minutos são  equivalentes a {horas}')
