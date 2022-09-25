from operator import itemgetter
from random import randint
from time import sleep

dados = {
    "jogador 1": randint(1, 6),
    "jogador 2": randint(1, 6),
    "jogador 3": randint(1, 6),
    "jogador 4": randint(1, 6),
}

for key, index in dados.items():
    print(f"{key.capitalize()} tirou {index}.")
    sleep(0.5)

print("=" * 35)
print("RANKING:".center(35))
for index, value in enumerate(sorted(dados.items(), key=itemgetter(1), reverse=True)):
    print(f"{index + 1}º Lugar: {value[0]} com {value[1]} pontos.")