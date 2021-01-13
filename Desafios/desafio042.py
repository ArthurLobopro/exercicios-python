from datetime import date
ano = date.today().year
nascimento = int(input('Digite seu ano de nascimento:  '))
idade = ano-nascimento
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
