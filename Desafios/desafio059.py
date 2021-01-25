opcao = 0
n1 = int(input('Primeiro número:  '))
n2 = int(input('Segundo número:  '))
while opcao != 5:
    print('\nO que deseja fazer?')
    opcao = int(input('\n[1] Somar.\n[2] Multiplicar.\n[3] Maior.\n[4] Trocar números.\n[5] Sair.\n'))
    if opcao == 1:
        print('\n{} + {} = {}'.format(n1,n2,n1+n2))
    if opcao == 2:
        print('\n{} * {} = {}'.format(n1,n2,n1*n2))
    if opcao == 3:
        maior = n1 if n1>n2 else n2
        print(f'\nEntre os números {n1} e {n2} o maior é {maior}')
    if opcao == 4:
        n1 = int(input('Primeiro numero:  '))
        n2 = int(input('Segundo numero:  '))