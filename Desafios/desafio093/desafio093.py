jogador = {}

jogador["nome"] = input("Nome do jogador: ")
jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador["gols"] = []

for i in range(jogador["partidas"]):
    jogador["gols"].append(int(input(f"Quantos gols {jogador['nome']} fez na {i+1}ª partida?  ")))

jogador["total_gols"] = sum(jogador["gols"])

print("="*40)
print(f"O jogador {jogador['nome']}, em {jogador['partidas']} partidas, realizou {jogador['total_gols']} gols:")
for index, gol in enumerate(jogador["gols"]):
    print(f"{index + 1}ª partida: {gol} gols.")