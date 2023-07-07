def area(l: float, c: float):
    return l * c

LARGURA = float(input("Informe a largura (m):  ").strip())
CUMPRIMENTO = float(input("Informe o cumprimento do terreno (m):  ").strip())
AREA = area(LARGURA, CUMPRIMENTO)

print(f"A área de um terreno com as proporções {CUMPRIMENTO}m x {LARGURA}m é de {AREA}m²")