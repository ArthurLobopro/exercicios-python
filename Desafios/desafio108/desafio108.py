from moeda import aumentar, diminuir, moeda

value = float(input("Digite o valor do produto:  ").strip())

cartao = aumentar(value, 1.5)
a_vista = diminuir(value, 8)

print(f"Com o cartão você pagará 1,5% mais caro: {moeda(cartao)}")
print(f"Pagando a vista você ganha 8% de desconto: {moeda(a_vista)}")
