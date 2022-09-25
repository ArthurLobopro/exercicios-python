aluno = {}

aluno["Nome"] = input("Nome: ").strip()
aluno["Média"] = float(input("Média: ").strip())
aluno["Situação"] = "Aprovado" if aluno["Média"] >= 7 else "Recuperação" if aluno["Média"] >= 5 else "Reprovado"

print("="*35)
for key, value in aluno.items():
    print(f"{key}: {value}")