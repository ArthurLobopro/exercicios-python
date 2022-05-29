nomes = []
precos = []
mais_de_1000 = 0
nome_barato = ""
preco_barato = 0

while True:
    nome = input("Nome do Produto:  ").strip()
    preco = float(input("Preço do produto: R$").strip().replace(",","."))

    if len(nomes) == 0 or preco < preco_barato:
        nome_barato = nome
        preco_barato = preco

    if preco > 1000:
        mais_de_1000 += 1


    nomes.append(nome)
    precos.append(preco)
    if input("Deseja continuar ? [S/N]: ").strip().upper() != "S":
        break
    print("")

print(f"Total: {sum(precos):.2f}")
print(f"Quantidade de produtos mais caros que R$1000: {mais_de_1000}")
print(f"Produto mais barato: {nome_barato}, custando R${preco_barato:.2f}")