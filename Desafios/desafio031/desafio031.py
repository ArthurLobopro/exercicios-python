km = float(input('Digite quantos quilômetros têm a viagem:\n'))
custo = km*0.50 if km<=200 else km*0.45
print('Sua passagem irá custar RS{:.2f}'.format(custo))