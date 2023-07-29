def escreva(text: str):
    text_len = len(text)
    space = 3
    bar_len = (text_len + space * 2)
    bar = "~" * bar_len
    print(bar)
    print(text.center(bar_len))
    print(bar)

escreva("Arthur Lobo")
escreva("Curso de Python")
escreva("097.py")