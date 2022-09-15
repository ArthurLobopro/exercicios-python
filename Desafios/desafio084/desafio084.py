pessoas = []

maior_peso = []
menor_peso = []

while True:
    nome = input("Nome: ").strip()
    peso = float(input("Peso: ").strip())

    pessoas.append([nome, peso])

    if len(maior_peso) == 0:
        maior_peso.append(peso)
        maior_peso.append(nome)
    elif peso > maior_peso[0]:
        maior_peso.clear()
        maior_peso.append(peso)
        maior_peso.append(nome)
    elif peso == maior_peso[0]:
        maior_peso.append(nome)

    if len(menor_peso) == 0:
        menor_peso.append(peso)
        menor_peso.append(nome)
    elif peso < menor_peso[0]:
        menor_peso.clear()
        menor_peso.append(peso)
        menor_peso.append(nome)
    elif peso == menor_peso[0]:
        menor_peso.append(nome)

    if input("Deseja continuar? [s/n] ").strip().lower() != "s":
        break

print("="*30)
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"O menor peso foi de {menor_peso[0]}kg, percencente a: {menor_peso[1:]}")
print(f"O maior peso foi de {maior_peso[0]}kg, pertencente a: {maior_peso[1:]}")