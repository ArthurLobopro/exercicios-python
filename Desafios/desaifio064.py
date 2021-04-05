nuns = []
num = 0
while num != 999:
    num = int(input("Digite um numero: "))
    if num != 999:
        nuns.append(num)
print("Números digitados: ")
print(str(nuns).replace("[","").replace("]",""))
print("Soma dos números: ")
print(sum(nuns))