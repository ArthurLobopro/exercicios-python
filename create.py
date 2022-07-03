from os import mkdir , write, path

print(path.abspath(__file__))

number = input("Digite o número do exercício: ")

if len(number) == 2:
    number = f"0{number}"


DIRNAME = f'./Desafios/desafio{number}'

README_PATH = path.join(DIRNAME, "README.md")

README_CONTENT = (f"""# DESAFIO{number}

## Enunciado""")

PYTHON_NAME = path.join(DIRNAME, f"desafio{number}.py")

mkdir(DIRNAME)

README_FILE = open(README_PATH, "w")
README_FILE.write(README_CONTENT)
README_FILE.close()

open(PYTHON_NAME, "w").close()