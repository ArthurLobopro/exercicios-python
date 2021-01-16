from modules.cores import creturn,cprint
peso = float(input('Digite seu peso em kg:\n'))
altura = float(input('Digite sua altura: \n'))
imc = peso/altura**2
print(f'Seu IMC é {imc:.2f}')
if imc<18.5:
    print('Você está {} do peso'.format(creturn('ABAIXO',c='red')))
elif imc<=25 :
    print('Você tem um peso ',creturn('Ideal.',c='green'))
else:
    print('Você tem ',end='') 
    if imc<=30:
        cprint('SOBREPESO.',c='yellow')
    elif imc<=40:
        cprint('OBESIDADE',c='red')
    else:
        cprint('OBESIDADE MÓRBIDA',c='red')