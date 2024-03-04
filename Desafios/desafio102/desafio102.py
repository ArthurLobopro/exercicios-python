from re import sub
from random import randint


def fatorial(num, show=False):
    calc_arr = list(range(num, 0, -1))
    fat = 1

    for value in calc_arr:
        fat *= value

    if (show):
        operation = str(calc_arr).replace(", ", " x ")
        operation = sub(
            r"\[|\]", "", operation)

        print(f"{operation} = ", end="")

    print(fat)


def line():
    print("--"*20)


line()
fatorial(randint(0, 10))
line()
fatorial(randint(0, 10), True)
