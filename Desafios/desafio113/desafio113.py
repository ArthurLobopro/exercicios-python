from modules.cores import cprint


def readInt(message="Digite um número inteiro:  "):
    while True:
        try:
            data: str = input(message).strip()
            return int(data)
        except KeyboardInterrupt:
            cprint("\nO usuário preferiu não informar esse valor", "blue")
            return 0
        except:
            cprint(f"'{data}' não é um número inteiro válido", "red")


def readFloat(message="Digite um número decimal:  "):
    while True:
        try:
            data: str = input(message).strip().replace(",", ".")
            converted = float(data)

            if converted.is_integer():
                raise Exception()

            return converted
        except KeyboardInterrupt:
            cprint("\nO usuário preferiu não informar esse valor", "blue")
            return 0
        except:
            cprint(f"'{data}' não é um número decimal válido", "red")


INT = readInt("Digite um número inteiro:  ")
FLOAT = readFloat("Digite um número decimal:  ")

print(f"O valor inteiro digitado foi {INT} e o valor decimal foi {FLOAT}")
