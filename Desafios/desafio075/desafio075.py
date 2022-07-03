tupla = ()
pares = ()

for i in range(0,4):
    num = int(input(f"Digite o {i + 1}° número:  ").strip())
    tupla += tuple([num])
    if num % 2 == 0:
        pares += tuple([num])

print(f"Valores fornecidos: {tupla}.")
print(f"O número 9 apareceu {tupla.count(9)} vez(es).")
try:
    print(f"O primeiro número 3 foi digitado na posição: {tupla.index(3) + 1}.")
except:
    print("O número 3 não foi informado.")
print(f"Valores pares fornecidos: {pares}.")