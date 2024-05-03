from os import get_terminal_size
from modules.cores import creturn
from typing import Callable

TERMINAL_WIDTH = get_terminal_size().columns
TABLE_WIDTH = TERMINAL_WIDTH if (
    TERMINAL_WIDTH // 2) < 50 else TERMINAL_WIDTH // 2


def line():
    print("-"*TABLE_WIDTH)


def title(content: str, firstLine=True, lastLine=True):
    if firstLine:
        line()

    print(content.center(TABLE_WIDTH))

    if lastLine:
        line()


def readString(message: str, onError):
    while True:
        try:
            value = input(message).strip()

            if len(value) > 0:
                return value
            else:
                raise Exception("Invalid String")
        except:
            onError(value)


def defaultReadintOnError():
    raise Exception("Inteiro inválido")


def readInt(
    message,
    validate: Callable[[int], bool] = lambda: True,
    onError: Callable[[], None] = defaultReadintOnError
):
    while True:
        try:
            data: str = input(message).strip()
            data = int(data)

            if validate(data):
                return data
            else:
                onError(data)
        except:
            onError(data)


def readOpt(optSize):
    def validate(x): return x > 0 and x < (optSize + 1)

    def onError(data):
        title(creturn(f"'{data}' não é uma opção válida", "red"))

    VAL = readInt("Sua opção:  ", validate, onError)
    line()
    return VAL
