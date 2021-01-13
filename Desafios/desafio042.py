idade = int(input('Digite sua idade:  '))
print('Sua categoria de atleta é: ',end='')
if idade>0 and idade<=9:
    print('MIRIM.')
elif idade<=14:
    print('INFANTIL.')
elif idade<=19:
    print('JÚNIOR.')
elif idade<=25:
    print('SÊNIOR.')
else:
    print('MASTER.')
