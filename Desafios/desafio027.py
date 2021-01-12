nome = input('Digite seu nome completo:\n').strip()
nome = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(nome[0],nome[len(nome)-1]))