import enum


def print_arr(arr: list, custom_end="\n"):
    for i,v in enumerate(arr):
        end= custom_end if len(arr) == i+1 else ", "
        print(v, end=end)

sequencia = []

for i in range(5):
    sequencia.append(int(input(f"Digite o {i+1}° número: ")))

maior = sequencia[0]
menor = sequencia[0]

posicoes_maior = []
posicoes_menor = []

for i,v in enumerate(sequencia):
    if v > maior:
        maior = v
        posicoes_maior = [i]
    elif v == maior:
        posicoes_maior.append(i)

    if v < menor:
        menor = v
        posicoes_menor = [i]
    elif v == menor:
        posicoes_menor.append(i)

print("="*30)
print("Você digitou os valores: ")
print_arr(sequencia)

print(f"O maior número digitado foi {maior}, nas posições: ", end="")
print_arr(posicoes_maior, custom_end=".\n")
print(f"O menor número digitado foi {menor}, nas posições: ", end="")
print_arr(posicoes_menor, custom_end=".\n")
