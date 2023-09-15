
def inverter(numero):
    u = numero % 10
    print("u:",u)
    numero =  numero //10
    print("numero:",numero)
    d =  numero % 10
    print("d:",d)
    numero =  numero // 10
    print("numero:",numero)
    c = numero % 10
    print("c:",c)
    numero = numero // 10
    print("numero:",numero)
    m = numero % 10
    print("m:",m)
    numero_investido = (u* 1000)+ (d*100)+(c*10)+ m
    print("numero_investido:",numero_investido)
    return numero_investido

n = int(input("digite um numero entre 1000 e 9999:"))

print(f'o Inverso  de {n} é  {inverter(n)}')
