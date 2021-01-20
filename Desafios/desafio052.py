from modules.cores import creturn
num = int(input('Digite um número: '))
divs = list(range(1,num+1))
print (str(divs).replace('[','').replace(']',''))
for i in range(1,num+1):
    if num%i==0:
        print(creturn(str(i),c='green'),end=' ')
    else:
        print(creturn(str(i),c='red'),end=' ')
        divs.remove(i)
if len(divs)==2:
    print('\n{} é divisível apenas por 2 números então ele É um número PRIMO'.format(num))
else:
    print('\n{} é divisível por {} números então ele NÃO É um número PRIMO'.format(num,len(divs)))
