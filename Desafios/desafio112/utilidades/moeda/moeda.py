from os import get_terminal_size


def dobro(val, isFormated=False):
    result = val * 2
    return moeda(result) if isFormated else result


def metade(val, isFormated=False):
    result = val / 2
    return moeda(result) if isFormated else result


def aumentar(val, percentage, isFormated=False):
    result = val + (val * percentage / 100)
    return moeda(result) if isFormated else result


def diminuir(val, percentage, isFormated=False):
    result = val - (val * percentage / 100)
    return moeda(result) if isFormated else result


def moeda(val):
    return f"R${val:.2f}"


TERMINAL_SIZE = get_terminal_size().columns
TABLE_SIZE = TERMINAL_SIZE//2


def line():
    print("-"*TABLE_SIZE)


def spaceBetween(left: str, right: str):
    size = TABLE_SIZE - len(right + left)
    print(f"{left}{(' ' * size)}{right}")


def resumo(val, aumento, desconto):
    line()
    print("TABELA DE PAGAMENTO".center(TABLE_SIZE))
    line()
    spaceBetween("Preço Base:", moeda(val))
    spaceBetween("Preço no Cartão:", aumentar(val, aumento, True))
    spaceBetween("Preço à Vista:", diminuir(val, desconto, True))
    line()
