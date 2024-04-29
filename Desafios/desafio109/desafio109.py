from moeda import aumentar, diminuir

value = float(input("Digite o valor do produto:  ").strip())

cartao = aumentar(value, 1.5, True)
a_vista = diminuir(value, 8, True)

print(f"Com o cartão você pagará 1,5% mais caro: {cartao}")
print(f"Pagando a vista você ganha 8% de desconto: {a_vista}")
