from modules.cores import creturn
n1 = float(input('Digite a primeira nota:  '))
n2 = float(input('Digite a segunda nota:  '))
media = (n1+n2)/2
print('Com as notas {} e {} o aluno obteve a média de: {}'.format(n1,n2,media))
if media>=7:
    print('O aluno está {}.'.format(creturn('APROVADO',c='green')))
elif media>=5:
    print('O aluno está de {}.'.format(creturn('RECUPERAÇÃO',c='yellow')))
else:
    print('O aluno está {}.'.format(creturn('REPROVADO.',c='red')))
