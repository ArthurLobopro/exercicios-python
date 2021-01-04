# fiz esta função porque o split em JS quabra toda a string em caracteres e não sabia que exisita a função list() para fazer isso.
def mysplit(string):
    lista= ['']
    lista.extend(string)
    lista.remove('')
    return lista

num = str(input("Digite um número entre 0 e 9999:\n")).strip()
#Para usar esta função basta aoagar o comentário da linha abaixo e comentar a linha 12
#num = mysplit(num)
num = list(num)
num.reverse()
valores = ['Unidade: ', 'Dezena: ', 'Centena: ', 'Milhar: ']
for i in range(0,len(num)):
    print('{}{}'.format(valores[i],str(num[i])))
