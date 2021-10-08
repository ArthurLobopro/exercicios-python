from os import system
def clear():
    system('clear || cls')
def progrecao(i,f,end=False):
    soma = prim
    while i<f:
        print(soma, end= ' - ')
        soma += raz
        i+=1
        if i == f and end == False:
            acres = int(input('\nQuantos termos a mais você deseja?  '))
            f += acres
            if acres == 0:
                clear()
                print(f'Exibindo progreção completa com {i} componentes')
                i=0
                return f

prim = int(input('Digite o primeiro termo da progreção:  '))
raz = int(input('Digite a razão dessa progreção:  '))
inicio = 0
fim = 10
fim = progrecao(inicio,fim)
progrecao(inicio,fim,True)
print('Fim.')