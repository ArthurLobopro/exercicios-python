quant = int(input("Informe quantos numeros de fibonacci voce deseja: "))
n1 = 0
n2 = 1
contador = 0

while (contador < quant):
    print(f"{n1}", end= "-" if contador+1 != quant else "\n")
    [n1,n2] = [n2, n1 + n2]
    contador+=1
