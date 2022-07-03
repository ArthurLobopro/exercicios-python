from random import randint

aleatorios = (
    randint(0,20),
    randint(0,20),
    randint(0,20),
    randint(0,20),
    randint(0,20)
)

maior = menor = aleatorios[0]

for num in aleatorios:
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num

print(f"Números sorteados: {aleatorios}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")