from modules.cores import cprint


def leiaDinheiro(msg):
    while True:
        value = input(msg).strip().replace(",", ".")
        try:
            return float(value)
        except:
            cprint(f"Erro: '{value}' não é um preço válido!", "red")
