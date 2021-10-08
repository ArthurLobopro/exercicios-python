a = float(input('Digite o tamanho da reta a:\n'))
b = float(input('Digite o tamanho da reta b:\n'))
c = float(input('Digite o tamanho da reta c:\n'))
if (a+b>c and b+c>a and c+a>b):
    print('Estas retas podem formar um triângulo.')
else:
    print('Estas retas não podem formar um triângulo.')