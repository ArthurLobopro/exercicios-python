nuns = []
num = 0
while num != 999:
    num = int(input("Digite um numero (999 para parar):"))
    if num != 999:
        nuns.append(num)
print(f"Você informou um total de {len(nuns)} números, sendo eles: ")
print(str(nuns).replace("[","").replace("]",""))
print("Soma dos números: ")
print(sum(nuns))