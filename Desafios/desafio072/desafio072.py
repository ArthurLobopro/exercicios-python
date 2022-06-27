extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    num = int(input("Digite um número entre 0 e 20:  "))
    if num >= 0 and num <=20:
        print(f"{num} por extenso é {extenso[num]}")
        break
    else:
        print(f"{num} não está no intervalo entre 0 e 20, tente novamente.")