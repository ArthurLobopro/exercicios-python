from modules.cores import creturn
from random import randint

def win():
    print('Você {}'.format(creturn('VENCEU!!!',c='green')))
def lose():
    print('Você {}'.format(creturn('PERDEU!!!',c='red')))
def empate():
    print('Deu {}'.format(creturn('EMPATE',c='yellow')))

options = ['pedra','papel','tesoura']
print('Opções:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura')
jogador = int(input("Qual sua jogada?  ")) 
computador = options[randint(0,2)]
if jogador >=0 and jogador<=2:
    jogador = options[jogador]
    print('Você escolheu {} e o computador {}'.format(jogador,computador))
    if jogador == computador:
        empate()
    else:
        if jogador == 'pedra':
            if computador == 'tesoura':
                win()
            else: 
                lose()
        if jogador == 'papel':
            if computador == 'pedra':
                win()
            else: 
                lose()
        if jogador == 'tesoura':
            if computador == 'papel':
                win()
            else: 
                lose()
else:
    print('Opção inválida,tente novamente!')