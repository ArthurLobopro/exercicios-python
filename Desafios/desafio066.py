from os import system
quant = 0
soma = 0

while True:
    num = int(input("Digite um número para soma [999 para parar]:  "))
    system("cls")
    if num == 999:
        break
    quant += 1
    soma += num

print(
f"""Quantidade de números digitados: {quant}
Soma dos números: {soma}"""
)