def le(num):
    return float(input(f'Peso da {num} pessoa:  '))
pesos = [le(1),le(2),le(3),le(4),le(5)]
pesos.sort()
print("O maior peso lido foi de {}Kg.".format(pesos[4]))
print('O menor peso lido foi de {}Kg.'.format(pesos[0]))
