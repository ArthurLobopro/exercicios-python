from random import randint


def line():
    print("-="*30)


def maior(*args: int):
    line()
    print("Analisando valores obtidos...")

    lenght = len(args)

    greater = args[0] if lenght > 0 else 0

    for value in args:
        print(value, end=" ")
        if (value > greater):
            greater = value

    print(f"Foram informados {lenght} valores ao todo.")
    print(f"O maior valor informado foi {greater}.")


def getRandomValues(len: int = 5):
    values = []
    for i in range(len + 1):
        values.append(randint(0, 20))
    return values


maior(*getRandomValues(randint(0, 10)))
maior(*getRandomValues(randint(0, 10)))
maior(*getRandomValues(randint(0, 10)))
maior()
