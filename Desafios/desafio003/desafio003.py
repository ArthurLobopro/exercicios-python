n1 = float(input("Digite um número:\n"))
n2 = float(input("Digite outro número:\n"))
soma = n1+n2
#if else apenas para deixar a resposta bonita...
if n1.is_integer() == True:
    n1 = int(n1)
if n2.is_integer() == True:
    n2 = int(n2)
if soma.is_integer() == True:
    soma = int(soma)
print("{} + {} = {}".format(n1, n2, soma))
