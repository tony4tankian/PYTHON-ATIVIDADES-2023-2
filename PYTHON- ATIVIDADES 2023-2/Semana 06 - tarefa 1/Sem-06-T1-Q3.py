Rsegundos = int(input(""))
minutos = Rsegundos//60
segundos = Rsegundos % 3600

segundos = segundos % 60
horas = minutos //60
minutos = minutos % 60

print(f'{horas}:{minutos}:{segundos}')


