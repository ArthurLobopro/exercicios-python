from datetime import datetime
maior = 0
menor = 0
ano_atual = datetime.today().year
for i in range(0,7):
    ano = int(input('Em que ano a {}ª pessoa nasceu?\n'.format(i+1)))
    idade = ano_atual-ano
    if (idade>=18):
        maior+= 1 
    else:
        menor+=1
print('Ao todo temos {} maiores de idade e {} menores de idade.'.format(maior,menor))