prim = int(input('Digite o primeiro termo da progreção:  '))
raz = int(input('Digite a razão dessa progreção:  '))
i = 0
soma = prim
while i<10:
    print(soma, end= ' - ' if i < 9 else ' - Fim.')
    soma += raz
    i+=1