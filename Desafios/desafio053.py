def replaceAll(string,old=' ',new=''):
    string=str(string)
    while string.count(' ')!=0:
        string=string.replace(old,new)
    return string

frase = str(input('Digite uma frase:  ')).strip()
frase = replaceAll(frase)
reverse = ''
for i in range(len(frase)-1,-1,-1):
    reverse+=frase[i]
print('O inverso de {} é {}.'.format(frase,reverse))
print('Temos um palíndromo' if frase==reverse else 'Esta frase não é um palíndromo')

