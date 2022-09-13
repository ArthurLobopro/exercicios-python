expression = input("Digite a expressão: ").strip()

mount = []

def validate():
    for char in expression:

        if char == "(":
            mount.append(char)

        if char == ")":
            if len(mount) > 0:
                mount.pop()
            else:
                return print("A expressão é inválida.")

    if len(mount) == 0:
        print("A expressão é válida.")
    else: 
        print("A expressão é inválida.")

validate()