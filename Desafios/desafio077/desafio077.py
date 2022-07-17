palavras = (
    "Arthur", "Cipriano", "Lobo", "de", "Carvalho"
)

vogais = ("a","e","i","o","u")

def countVogais(palavra: str):
    count = 0
    for vogal in vogais:
        count  += palavra.lower().count(vogal)
    return count

def listVogais(palavra: str):
    lista_vogais = []
    for vogal in vogais:
        if vogal in palavra.lower():
            lista_vogais.append(vogal)
    return lista_vogais

for palavra in palavras:
    print(f"A palavra '{palavra}' tem {countVogais(palavra)} vogais: {listVogais(palavra)} ")