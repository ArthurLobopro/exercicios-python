prim = int(input('Digite o primeiro termo da progreção:  '))
raz = int(input('Digite a razão dessa progreção:  '))
soma = prim
pa = list(range(prim,(prim+10)*raz,raz))
pa = str(pa).replace('[','').replace(']','')
print(f'Progreção:\n{pa}')