jogadores = []


def lerJogador():
    jogador = {}
    jogador["nome"] = input("Nome do jogador: ")
    jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador["gols"] = []

    for i in range(jogador["partidas"]):
        jogador["gols"].append(
            int(input(f"Quantos gols {jogador['nome']} fez na {i+1}ª partida?  "))
        )

    jogador["total_gols"] = sum(jogador["gols"])
    return jogador

def line():
    print("-" * 50)

def show_table():
    line()
    print(f"ID {'nome'.ljust(20)} {'gols'.ljust(20)} total")
    line()
    for index, jogador in enumerate(jogadores):
        print(f"{str(index+1).rjust(2)} {jogador['nome'].ljust(20)} {str(jogador['gols']).ljust(20)} {str(jogador['total_gols']).ljust(5)}")
    line()

def show_jogador(jogador):
    print(f"  Aproveitamento de {jogador['nome']}.  ".center(50, "-"))
    for i,v in enumerate(jogador["gols"]):
        print(f"No {i+1}° jogo: {v} gols.")
    line()

# print("=" * 40)
# print(
#     f"O jogador {jogador['nome']}, em {jogador['partidas']} partidas, realizou {jogador['total_gols']} gols:"
# )
# for index, gol in enumerate(jogador["gols"]):
#     print(f"{index + 1}ª partida: {gol} gols.")

while True:
    jogadores.append(lerJogador())
    if input("'Deseja continuar? [S/n] ").lower() != "s":
        break

show_table()

while True:
    jogador = int(input("Deseja ver o aproveitamento de qual jogador? (0 cancela) "))
    if jogador == 0:
        break
    else:
        show_jogador(jogadores[jogador-1])