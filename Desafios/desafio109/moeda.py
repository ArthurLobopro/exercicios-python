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
