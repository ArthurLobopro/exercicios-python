from random import randint
alunos = [input('Primeiro aluno: '),input('Segundo aluno: '),input('Terceiro aluno: '),input('Quarto aluno: ')]
#Leitura direta dos nomes
print('O aluno escolhido foi {}'.format(alunos[randint(0,3)]))
