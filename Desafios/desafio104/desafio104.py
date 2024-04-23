def readInt(message = ""):
    data: str = input(message).strip()
    
    try:
        number = int(data)
        return number
    except:
        print(f"'{data}' não é um número inteiro")
        return readInt(message) 

NUM = readInt("Digite um número inteiro:  ")
print(f"Você digitou {NUM}")