def ficha(name = "<desconhecido>", gols = 0):
    print(f"O jogador {name} fez {gols} gol(s) no campeonato.")

name = input("Nome do jogador:  ").strip() or "<desconhecido>"
gols: str = input("Número de gols:  ").strip() or "0"

if not gols.isnumeric():
    gols = 0

ficha(name, gols)
