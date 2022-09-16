matrix = [[], [], []]
soma_pares = 0
soma_3_coluna = 0
maior = 0

for linha in range(3):
    for coluna in range(3):
        num = int(input(f"Informe o número para posição ({linha+1},{coluna+1}): "))
        matrix[linha].append(num)

        if num % 2 == 0:
            soma_pares+=num
        if coluna == 2:
            soma_3_coluna+=num
        if linha == 1:
            if coluna == 1 or num> maior:
                maior = num

print("="*40)
for linhas in matrix:
    for coluna in linhas:
        print(f"[{str(coluna).center(5)}]", end=" ")
    print()

print("="*40)
print(f"Soma dos valores pares: {soma_pares}.")
print(f"Soma da 3ª coluna: {soma_3_coluna}.")
print(f"Maior valor da 2ª linha: {maior}.")