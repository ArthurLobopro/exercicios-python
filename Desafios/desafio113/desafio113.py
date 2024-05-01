def readInt(message=""):
    while True:
        data: str = input(message).strip()
        try:
            return int(data)
        except:
            print(f"'{data}' não é um número inteiro válido")


def readFloat(message=""):
    while True:
        try:
            data: str = input(message).strip().replace(",", ".")
            converted = float(data)

            if converted.is_integer():
                raise Exception()

            return converted
        except:
            print(f"'{data}' não é um número decimal válido")


INT = readInt("Digite um número inteiro:  ")
FLOAT = readFloat("Digite um número decimal:  ")

print(f"O valor inteiro digitado foi {INT} e o valor decimal foi {FLOAT}")
