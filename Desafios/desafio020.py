from random import shuffle
alunos = [input('Primeiro aluno: '),input('Segundo aluno: '),input('Terceiro aluno: '),input('Quarto aluno: ')]
shuffle(alunos)
print("A ordem sorteda foi:")
print('{}, {}, {}, {}.'.format(alunos[0],alunos[1],alunos[2],alunos[3]))