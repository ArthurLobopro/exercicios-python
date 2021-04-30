from random import randint
from os import system
vitorias = 0
while True:
    tipo = input("Par ou impar?  ").strip().lower()
    num = int(input("Número: "))
    num += randint(0,5)
    if tipo == "par" and num % 2 != 0:
        break
    if tipo != "par" and num % 2 == 0:
        break
    print("Você venceu!")
    vitorias += 1
system("cls")
print(f"""Você perdeu!\nVitórias consecutivas: {vitorias}""")
