salario = float(input('Digite seu salário:\nR$'))
salario+= salario*10/100 if salario>1250 else salario*15/100
print('Seu novo salário é de R${:.2f}'.format(salario))