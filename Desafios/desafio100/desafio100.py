from random import randint
from re import sub


def getRandomValues(len: int = 5):
    values = []

    for i in range(len + 1):
        values.append(randint(0, 20))

    return values


def sumEven(arr: list[int]):
    sum = 0

    for value in arr:
        if value % 2 == 0:
            sum += value

    return sum


def getListString(arr: list):
    return sub(r"\[|\]", "", str(ARR))


ARR = getRandomValues(5)
print(f"Lista: {getListString(ARR)}")
print(f"Soma dos elementos pares: {sumEven(ARR)}")
