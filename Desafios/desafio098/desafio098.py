from re import sub


def contador(FROM, TO, interval=1):
    print(f"Contando de {FROM} até {TO} de {interval} em {interval}")

    if FROM > TO and interval > 0 or FROM < TO and interval < 0:
        interval *= -1

    # range doesn't includes the last term, to we need an aditional
    aditional = -1 if FROM > TO else 1

    ARR = list(range(FROM, TO + aditional, interval))
    print(sub(r"\[|\]", "", str(ARR)), "Fim!")


def line():
    print("-="*20)


line()

contador(1, 10)
line()

contador(10, 0, 2)
line()

print("Agora é sua vez de personalizar a contagem!")
FROM = int(input("Início: "))
TO = int(input("FIM: "))
PASS = int(input("Passo: "))
line()

contador(FROM, TO, PASS)
