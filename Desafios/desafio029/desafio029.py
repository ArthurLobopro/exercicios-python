vel = float(input('Digite a velocidade: \n'))
if vel<=80:
    print('Sua velocidade está dentro do limite')
else:
    print('Você ultrapassou o limite de velocidade e terá que pagar uma multa de R${:.2f}'.format((vel-80)*7))