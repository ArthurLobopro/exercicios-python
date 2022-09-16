from random import randint

quant = int(input(f"Quantos jogos deseja gerar? "))

palpites = []

def geraPapalpite():
    palpite = []
    while len(palpite) < 6:
        num = randint(1,60)
        if num not in palpite:
            palpite.append(num)
    return palpite

for i in range(quant):
    print(f"Jogo {i+1}: {geraPapalpite()}")