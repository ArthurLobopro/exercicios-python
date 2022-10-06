pessoas = []

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Informe seu sexo: [M/F] ").upper()
    pessoas.append({"nome":nome, "idade": idade, "sexo": sexo})
    if input("Deseja continuar? [S/n] ").lower() != "s":
        break

pessoas_quant = len(pessoas)
media_idade = 0
mulheres = []
for pessoa in pessoas:
    media_idade += pessoa["idade"]
    if pessoa["sexo"] == "F":
        mulheres.append(pessoa["nome"])
media_idade /= pessoas_quant

print("="*40)
print(f"Foram cadastradas {pessoas_quant} pessoas")
print(f"A média de idade foi de {media_idade}")
print("Mulheres cadastradas: ")
for mulher in mulheres:
    print(f"    {mulher}.")
print("Pessoas com idade acima da média: ")
for pessoa in pessoas:
    if  pessoa['idade'] > media_idade:
        print(f"   {pessoa['nome']}.")