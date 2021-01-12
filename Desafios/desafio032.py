ano = int(input('Digite um ano:\n'))
print('{} é um ano bissexto'.format(ano) if ano%4==0 else '{} não é um ano bissexto'.format(ano))