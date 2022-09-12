sequence = []

pares = []
impares = []

while True:
    num = int(input("Digite um número: ").strip())
    sequence.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    if input("Deseja continuar? [s/n] ").strip().lower() != "s":
        break

print("="*35)
print(f"Números digitados: {sequence}")
print(f"Números pares digitados: {pares}")
print(f"Números ímpares digitados: {impares}")