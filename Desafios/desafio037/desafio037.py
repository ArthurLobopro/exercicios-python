from modules.cores import creturn
num = int(input('Digite um número inteiro:  '))
print('Para qual base deseja converter este número?\nDigite:')
print('1. Para binário\n2. Para octal\n3. Para hexadecimal')
opcao = int(input('Sua opção:  '))
if opcao == 1:
    print('{} convertido para {} é igual a {}'.format(creturn(num,c='cyan') , creturn('BINÁRIO',c='green'), creturn(bin(num)[2:],c='blue')))
elif opcao==2:    
    print('{} convertido para {} é igual a {}'.format(creturn(num,c='cyan') , creturn('OCTAL',c='green'), creturn(oct(num)[2:],c='blue')))
elif opcao==3:
    print('{} convertido para {} é igual a {}'.format(creturn(num,c='cyan') , creturn('HEXADECIMAL',c='green'), creturn(hex(num)[2:].upper(),c='blue')))
else:
    print('Opção inválida, tente novamente')