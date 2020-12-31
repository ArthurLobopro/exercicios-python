dias = int(input("Quantos dias o carro ficou alugado?\n"))
km = float(input("Durante esses {} dias, quantos quilometros foram rodados?\n".format(dias)))*0.15
print("O preço do aluguel é de R${:.2f}".format(dias*60+km))
