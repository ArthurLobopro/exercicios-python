from modules.cores import creturn
from utils import line, title, readOpt, TABLE_WIDTH
from data import loadData, registry, dataAtual


ACTIONS = [
    {
        "text": "Cadastrar Pessoa",
        "action": lambda: register()
    },
    {
        "text": "Visualizar Cadastros",
        "action": lambda: showData()
    },
    {
        "text": "Sair",
        "action": lambda: menuExit()
    }
]


def register():
    registry()
    main()


def menuExit():
    title("Até Logo!")
    exit(0)


def menuOptions():
    for i, option in enumerate(ACTIONS):
        print(creturn(i+1, "yellow"), "-", creturn(option["text"], "blue"))

    line()


def showData():
    if len(dataAtual) > 0:
        for value in dataAtual:
            NAME_STR = value["name"]
            AGE_STR = f"{value['age']} anos"
            SPACE = TABLE_WIDTH - len(NAME_STR+AGE_STR)
            print(NAME_STR, AGE_STR, sep=" " * SPACE)
        else:
            main()
    else:
        print("Não existem dados cadastrados atualmente!")
        main()


def menu():
    title("MENU")
    menuOptions()


def main():
    menu()
    RES = readOpt(len(ACTIONS))
    ACTIONS[RES-1]["action"]()
