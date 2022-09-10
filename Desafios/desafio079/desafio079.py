again = True
sequence = []

while again:
    num = int(input("Digite um número: "))
    if not num in sequence:
        sequence.append(num)

    again = input("Deseja continuar? [s/n]: ").strip().lower() == "s"

sequence.sort()
print(f"Sequência obtida: {sequence}")