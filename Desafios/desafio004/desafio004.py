algo = input("Digite algo:\n")
print("O tipo primitivo de {} é {}".format(algo,type(algo)))
print("{} é numéroco? {}".format(algo, algo.isnumeric()))
print("{} é alfanumérico? {}".format(algo, algo.isalnum()))
print("{} é alfabético? {}".format(algo, algo.isalpha()))
print("{} é um dígito numérico? {}".format(algo, algo.isdigit()))
print("{} é escrito em minúsculas? {}".format(algo, algo.islower()))
print("{} é escrito em maiúsculas? {}".format(algo, algo.isupper()))
print("{} é um espaço? {}".format(algo, algo.isspace()))