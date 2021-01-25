from random import randint
sortnum = randint(0,10)
num = 6 
#Maior que o random
tentativas = 1
print('Tente  um número entre 0 e 10:')
while(num!=sortnum):
    num = int(input(''))
    if num==sortnum:
        print(f'Parabéns ! Você acertou em {tentativas} tentativas! O número sorteado foi {num}.')
    else:
        print('Você errou! Tente novamente:')
        tentativas+=1
