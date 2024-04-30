from utilidades.moeda import resumo
from utilidades.dado import leiaDinheiro


value = leiaDinheiro("Digite o valor do produto:  R$")

resumo(value, 1.5, 8)
