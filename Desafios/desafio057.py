sexo = ''
while(sexo!='M' and sexo !='F'):
    sexo = input('Informe seu sexo [M/F]:  ').strip().upper()
    if(sexo!='M' and sexo !='F'):
        print(f'Opção \'{sexo}\' inválida, verifique os dados e tente novamente!')
print(f'Sexo {sexo} registrado com sucesso!')