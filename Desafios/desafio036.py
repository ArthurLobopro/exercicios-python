from modules.cores import creturn
valor = float(input('Digite o valor da casa:\nR$'))
salario = float('Digite seu salário:\nR$')
meses = int(input('Em quantos meses você irá pagar o empréstimo?\n'))
prestação = valor/meses
if prestação>salario*30/100:
    print()