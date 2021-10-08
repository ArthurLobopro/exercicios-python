nuns = [int(input('Digite um número:\n')),int(input('Digite outro número:\n')),int(input('Digite outro número:\n'))]
maior = nuns[0]
menor = nuns[0]
if nuns[1]>maior: 
    maior=nuns[1]
elif nuns[1]<menor:
    menor=nuns[1]
if nuns[2]>maior: 
    maior=nuns[2]
elif nuns[2]<menor:
    menor=nuns[2]
print('Maior: {}\nMenor: {}'.format(maior,menor))