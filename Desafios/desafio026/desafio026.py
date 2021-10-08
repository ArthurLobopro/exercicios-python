frase = input('Digite uma frase:\n').strip()
ocorrencias = frase.lower().count('a')
primeiro = frase.lower().find('a') + 1
ultimo = frase.lower().rfind('a') + 1
print("Na frase {}".format(frase))
print("Há {} ocorrências da letra 'a'".format(ocorrencias))
print("A primeira ocorrência de 'a' acontece no {} dígito.\nA última ocorrência no {} dígito.".format(primeiro, ultimo))