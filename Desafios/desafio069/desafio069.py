from os import system
maior18 = 0
homens = 0
mulheresMenor20 = 0

while True:
    sexo = input("Informe seu sexo [M/F]: ").lower()
    idade = int(input("Informe sua idade: "))
    if idade>18:
        maior18 += 1
    if sexo == "f" and idade < 20:
        mulheresMenor20 += 1
    if sexo == "m":
        homens += 1
    if input("Deseja continuar os registros? S/N  ").lower() != "s":
        break
    system("cls")

system("cls")
print(f"""Registro terminado!
Foram registradas:
{maior18} pessoas maiores de 18 anos.
{homens} homens.
{mulheresMenor20} mulheres menores de 20 anos.""")