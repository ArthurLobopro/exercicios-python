preco = float(input('Digite o valor das compras:\nR$'))
print("""Escolha uma forma de pagamento:
1. à vista dinheiro/cheque.
2. à vista no cartão.
3. 2x no cartão.
4. 3x ou mais no cartão.""")
pagamento = int(input('Sua opção:  '))
if pagamento>=1 and pagamento<=4:
    if pagamento == 1:
        desconto = -10
    elif pagamento == 2:
        desconto = -5
    elif pagamento == 3:
        desconto = 0
    else:
        desconto = 20
    print('Sua compra de R${:.2f} irá custar R${:.2f}'.format(preco,preco+preco*desconto/100))
else:
    print('Opção inválida, tente novamente')