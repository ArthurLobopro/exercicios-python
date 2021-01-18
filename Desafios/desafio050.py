soma = 0
cont = 0
for i in range(6):
    num = int(input('Digite o {}° número:   '.format(i+1)))
    if num % 2 == 0:
        soma+= num
        cont += 1
print(f'A soma dos {cont} números pares fornecidos é: {soma}')