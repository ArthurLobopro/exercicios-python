from os import system
maior = menor = soma = num = int(input("Digite um número: "))
quant = 1
while num != "S":
    num = input("Para continuar digite um numero, para sair digite S:\n").strip().upper()
    if num != "S":
        num = int(num)
        quant += 1
        soma += num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
system("cls || clear")
print(
f"""Você digitou um total de {quant} números.
O maior némero digitado foi: {maior}
O menor número digitado foi: {menor}
A média dos numeros fornecidos é {soma/quant}""")