num = int(input('Digite o número para o fatorial:  '))
print(f'{num}! = ',end='')
fat = 1
for i in range(1,num+1):
    sinal = '=' if i==num else 'x'
    print(f'{i} {sinal}',end=' ')
    fat*=i
print(fat)