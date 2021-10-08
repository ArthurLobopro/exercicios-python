from os import system
def tabuada(num):
    print("_"*30)
    for i in range(0,11):
        print(f"{i} x {num} = {num*i}")
    print("_"*30)

while True:
    num = int(input("Informe um numero para gerar a tabuada [negativo para parar]:  "))
    if num < 0:
        system("cls")
        print("Programa encerrado.")
        break
    tabuada(num)