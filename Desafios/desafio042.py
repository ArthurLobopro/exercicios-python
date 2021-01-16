a = float(input('Digite o tamanho da reta a:\n'))
b = float(input('Digite o tamanho da reta b:\n'))
c = float(input('Digite o tamanho da reta c:\n'))
if (a+b>c and b+c>a and c+a>b):
    if a==b and b ==c:
        nome = 'equilátero'
    elif a==b or b==c or a == c:
        nome = 'isósceles'
    else:
        nome= 'escaleno'
    print('Estas retas podem formar um triângulo {}.'.format(nome))
else:
    print('Estas retas não podem formar um triângulo.')