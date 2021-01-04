cidade = input('Digite a cidade em que você nasceu:\n')
if cidade.lower().find('santo')==0:
    print('{} começa com "Santo"'.format(cidade))
else:
    print('{} não começa com "Santo"'.format(cidade))