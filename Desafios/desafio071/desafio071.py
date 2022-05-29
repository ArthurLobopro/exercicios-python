total = int(input("Informe o total a ser sacado: R$").strip())

notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0

while total >= 50:
    total -= 50
    notas_50 += 1

while total >= 20:
    total -= 20
    notas_20 += 1

while total >= 10:
    total -= 10
    notas_10 += 1

while total >= 1:
    total -= 1
    notas_1 += 1

print("Saque: ")
print(f"Notas de R$50: {notas_50}")
print(f"Notas de R$20: {notas_20}")
print(f"Notas de R$10: {notas_10}")
print(f"Notas de R$1: {notas_1}")
