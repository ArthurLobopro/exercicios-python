again = True
sequence = []

while again:
    sequence.append(int(input("Digite um número: ").strip()))
    again = input("Deseja continuar? [s/n] ").strip().lower() == "s"

sequence.sort(reverse=True)
have5 = "" if 5 in sequence else "não "
print(f"Você digitou {len(sequence)} números.")
print(f"Sequência em ordem decrescente: {sequence}")
print(f"A sequencia {have5}inclui o número 5.")