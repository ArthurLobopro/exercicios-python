from time import sleep
num = float(input('Digite um número:  '))
if num.is_integer()==True:
    num = int(num)
inicio = 0
fim = 10
passo = 1
opcao = int(input("""
Deseja fazer confugurações de inicio, fim ou intervalo da tabuada?
1. Para editar valores.
2. Usar valores padrão.
"""))
if opcao == 1:
    inicio = int(input('Digite o ínicio da tabuada:  '))
    fim = int(input('Digite o fim da tabuada:  '))
    passo = int(input('Digite o intervalo da tabuada:  '))
elif opcao ==2 :
    pass
else:
    print('Opção inválida, o programa será executado com os valores padrão.')
    sleep(3)
if inicio>fim and passo>0:
    passo = -passo
for i in range(inicio,fim+1,passo):
    print('{} x {} = {}'.format(num,i,num*i))