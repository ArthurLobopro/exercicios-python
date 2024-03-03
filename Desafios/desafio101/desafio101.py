from datetime import datetime


def voto(year):
    age = datetime.now().year - year

    if age < 16:
        return "VOTO NEGADO"

    if age >= 18:
        return "VOTO OBRIGATÓRIO"

    return "VOTO OPCIONAL"


year = int(input("Informe o ano do seu nascimento: "))
age = datetime.now().year - year

print(f"Com {age} anos: {voto(year)}.")
