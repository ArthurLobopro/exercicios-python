soma = 0
cont = 0
for i in range(0,500,3):
    if i%2!=0:
        soma+=i
        cont+=1
print('A soma de todos os {} múltiplos de 3 ímpares entre 1 e 500 é {}'.format(cont,soma))