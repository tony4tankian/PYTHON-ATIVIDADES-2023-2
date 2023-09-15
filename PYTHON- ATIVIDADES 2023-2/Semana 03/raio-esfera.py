raio = float(input(""))
pi = 3.141592
#float(input("Digite o valor do raio: "))

comprimento_circunferencia = 2 * pi * raio
area_circulo = pi * raio ** 2
area_esfera = 4 * pi * raio ** 2
volume_esfera = (4 / 3) * pi * raio ** 3

print(f"{comprimento_circunferencia:.6f}")
print(f"{area_circulo:.6f}")
print(f"{area_esfera:.6f}")
print(f"{volume_esfera:.6f}")
