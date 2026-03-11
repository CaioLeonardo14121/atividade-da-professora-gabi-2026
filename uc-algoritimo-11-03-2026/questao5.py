nome = input("Nome completo: ")
matricula = int(input("Digite a matrícula: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("\n--- RELATÓRIO ESCOLAR ---")
print(f"Aluno: {nome}")
print(f"Matrícula: {matricula}")
print(f"Média Final: {media:.2f}")