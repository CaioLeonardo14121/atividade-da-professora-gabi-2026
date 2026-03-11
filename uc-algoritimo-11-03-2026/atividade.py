# Entrada de dados
nome = input("Nome do aluno: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

# Criando o dicionário e calculando a média
aluno = {
    'nome': nome,
    'nota1': n1,
    'nota2': n2,
    'media': (n1 + n2) / 2
}

# Exibindo os dados
print(f"\nDados: {aluno}")
print(f"Média: {aluno['media']}")

# Verificando a situação
if aluno['media'] >= 7:
    print("Situação: Aprovado")
elif aluno['media'] >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")