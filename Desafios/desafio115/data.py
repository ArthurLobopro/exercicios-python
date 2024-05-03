import json
from os import path
from jsonschema import validate
from utils import readInt, readString, title
from modules.cores import cprint

FILEPATH = path.abspath(path.join(path.dirname(__file__), "./data.json"))

if not path.isfile(FILEPATH):
    open(FILEPATH, "w").close()


PERSONSCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    }
}

DATASCHEMA = {
    "type": "array",
    "items": PERSONSCHEMA
}

dataAtual = []


def loadData():
    global dataAtual
    try:
        with open(FILEPATH, "r") as FILE:
            dataAtual = json.loads(FILE.read())
    except:
        dataAtual = []
    finally:
        return dataAtual


def writeData(data):
    try:
        validate(data, DATASCHEMA)
        with open(FILEPATH, "w") as FILE:
            FILE.write(json.dumps(data))
            FILE.flush()
    except:
        print("Erro ao salvar o arquivo")


def sortData(data):
    return sorted(data, key=lambda x: x['name'])


def registry():

    def nomeOnError(data): cprint(f"'{data}' não é uma idade válida")
    nome = readString("Informe seu nome:  ", onError=nomeOnError)

    def idadeValidate(idade): return idade > 0 and idade < 100
    def idadeOnError(data): cprint(f"'{data}' não é uma idade válida")

    idade = readInt("Informe sua idade:  ", idadeValidate, idadeOnError)

    global dataAtual
    dataAtual.append({
        "name": nome,
        "age": idade
    })
    dataAtual = sortData(dataAtual)

    writeData(dataAtual)
    title("Cadastro feito!", lastLine=False)


loadData()
