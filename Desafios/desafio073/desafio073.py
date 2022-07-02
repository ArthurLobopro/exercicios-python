placares  = ("Palmeiras","Corinthians","Athletico-PR","Internacional","Atlético-MG","Fluminense","Santos","São Paulo","Flamengo","Botafogo","Avaí","Bragantino","Atlético-GO","Goiás","Ceará SC","Coritiba","América-MG","Cuiabá","Juventude","Fortaleza")

print("Primeiros 5 times:\n")
for [index, time] in enumerate(placares):
    if index == 5:
        print("")
        break

    print(f"{index + 1}. {time}")

print("Ultimos 4 colocados:\n")
for [index, time] in enumerate(reversed(placares)):
    if index == 4:
        print("")
        break
    print(f"{len(placares) - index}. {time}")

print("Times em ordem alfabética:\n")
for time in sorted(placares):
    print(time)

print("\nPosição do Chapecoense: \n")

try:
    index_chapecoense = placares.index("Chapecoense")
    print(f"Chapecoense está no {index + 1}° lugar!")
except:
    print("Chapecoense não está nos top 20 da seleção!")
