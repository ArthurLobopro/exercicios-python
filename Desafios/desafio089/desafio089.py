alunos = []

while True:
    aluno = [
        input("Nome: "),
        float(input("Nota 1: ").strip()),
        float(input("Nota 2: ").strip())
    ]

    alunos.append(aluno.copy())

    if input("Deseja continuar? [s/n] ").strip().lower() != "s":
        break

print("="*40, end="\n\n")
print("ID".ljust(3), "NOME".ljust(15), "MÉDIA".ljust(5))
print("-"*30)

for index, aluno in enumerate(alunos):
    print(
        f"{str(index + 1).ljust(3)}{str(aluno[0]).ljust(15)}{str(sum(aluno[1:3])/2).rjust(5)}")

print("="*40, end="\n\n")

while True:
    num = int(input("Mostrar notas de qual aluno? (0 para parar) ").strip())
    if num == 0:
        print("="*40, "\n", "Programa Finalizado!")
        break
    else:
        aluno = alunos[num-1]
        print(f"Notas de {aluno[0]}: {aluno[1:3]}")
