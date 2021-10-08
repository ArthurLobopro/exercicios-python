def pes(num):
    print('***** {}ª Pessoa *****'.format(num))
    nome = input('Nome:  ').strip()
    idade = int(input('Idade:  '))
    sexo = input('Sexo [M/F]:  ').upper()
    return [nome,idade,sexo]

pessoas = [pes(1),pes(2),pes(3),pes(4)]

soma = 0
mulh_jovs = 0
idade = 0
nome = ''
for i in range(0,4):
    soma+= pessoas[i][1]
    if(pessoas[i][2]=='F' and pessoas[i][1]<20):
        mulh_jovs+=1

    if(pessoas[i][2]=='M' and pessoas[i][1]>idade):
        idade = pessoas[i][1]
        nome = pessoas[i][0]


print('A média de idade do grupo é {} anos.'.format(soma/4))
print('O homem mais velho tem {} anos e chama-se {}.'.format(idade,nome))
print('Ao todo temos {} mulheres abaixo de 20 anos.'.format(mulh_jovs))
