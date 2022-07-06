LINE_WIDTH = 40


def line():
    print("-"*LINE_WIDTH)


produtos_e_precos = (
    "Caneta", 1.25,
    "Borracha", 0.75,
    "Grafites", 2,
    "Caderno", 14.99
)

precos_maxlength = 1

for i in range(1, len(produtos_e_precos), 2):
    length = len(str(produtos_e_precos[i]))
    if length + 3 >= precos_maxlength:
        precos_maxlength = length + 3

title = "Lista de Preços"
spaces = int((LINE_WIDTH - len(title))/2)

line()
print(f"{' ' * spaces}{title}{' ' * spaces}")
line()

for index,value in enumerate(produtos_e_precos):
    if index % 2 == 0:
        print(f"{value}{'.' * (LINE_WIDTH - len(value) - precos_maxlength)}", end="")
    else:
        formated_value = f"{value:.2f}"
        print(f"R${' ' * (precos_maxlength - 2 - len(formated_value))}{formated_value}")

line()