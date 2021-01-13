from modules.cores import cprint
#início do uso dos meus módulos
valor = float(input('Digite o valor da casa:\nR$'))
salario = float(input('Digite seu salário:\nR$'))
anos = int(input('Em quantos meses você irá pagar o empréstimo?\n'))
prestação = valor/(anos*12)
print('Para pagar uma casa de RS{:.2f} em {} anos a prestação será de R${:.2f}'.format(valor,anos,prestação))
print('O empréstimo foi',end=' ')
if prestação>salario*30/100:
    cprint('RECUSADO.',c='red')
else:
    cprint('CONCEDIDO.',c='green')