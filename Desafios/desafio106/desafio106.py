from cores import cprint
from os import get_terminal_size, environ

TERMINAL_SIZE = get_terminal_size().columns
environ["PAGER"] = "cat"


def getLine():
    return "~"*TERMINAL_SIZE


def section(text: str, bg):
    cprint(getLine(), "black", bg)
    cprint(text.center(TERMINAL_SIZE), "black", bg)
    cprint(getLine(), "black", bg)


def presentation():
    section("Sistema PyHelp", "green")


def end():
    section("Até mais!", "red")


def ajuda(cmd):
    # cprint("", color="white", bgcolor="blue", end="", reset=False)
    help(cmd)
    # cprint("", color="white", end="")


def main():
    while True:
        presentation()
        cmd = input("Função ou Biblioteca: ").strip()

        if cmd.lower() == "fim":
            end()
            break
        else:
            ajuda(cmd)


main()
