def percentual(valor,porcetagem):
    return valor * (porcetagem/100)

pr = float(input("Preço:"))
vr_p = float(input("Percentual:"))

pr_acres =  pr + percentual(pr,vr_p)

pr_desc = pr - percentual(pr,vr_p)



print(f'R${pr} com acrescime de {vr_p}% fica por R${pr_acres}')
print(f'R${pr} com desconto de {vr_p}% fica por R${pr_desc}')