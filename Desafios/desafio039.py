from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: \n'))
idade = ano_atual-nascimento
if idade < 18:
    print('Você ainda não tem idade para se alistar mas daqui a {} anos você poderá se alistar.'.format(18-idade))
elif idade>19:
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(idade-18,ano_atual-(idade-18)))
else:
    print('Você deve se alistar IMEDIATAMENTE!')