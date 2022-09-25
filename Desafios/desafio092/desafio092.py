from datetime import datetime

year = datetime.now().year
pessoa = {}

pessoa["nome"] = input("Nome: ").strip()
pessoa["idade"] = year - int(input("Data de Nascimento: ").strip())
pessoa["carteira de trabalho"] = int(
    input("Carteira de Trabalho (0 se não possui): ").strip()
)

if pessoa["carteira de trabalho"] != 0:
    pessoa["ano de contratação"] = int(input("Ano de Contratação: ").strip())
    pessoa["salário"] = float(input("Informe seu salário: ").strip())
    pessoa["aposenta com"] = (
        pessoa["idade"] + pessoa["ano de contratação"] + 35
    ) - year

print("=" * 35)
for key, value in pessoa.items():
    print(f"{key.capitalize()}: {value}")
