matrix = [[], [], []]

for i in range(3):
    for j in range(3):
        num = int(input(f"Informe o número para posição ({i+1},{j+1}): "))

        matrix[i].append(num)

print("="*40)
for linhas in matrix:
    for coluna in linhas:
        print(f"[{str(coluna).center(5)}]", end=" ")
    print()