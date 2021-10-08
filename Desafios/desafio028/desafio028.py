from random import randint
num = int(input('Digite um número entre 0 e 5:\t'))
sortnum = randint(0,5)
if num==sortnum:
    print('Você acertou!! O número sorteado foi ',num)
else:
    print('Você errou! O número sorteado foi ',sortnum)