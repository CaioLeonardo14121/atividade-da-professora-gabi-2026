senha = input("Digite sua senha: ")

# Verifica se tem 8 caracteres E se existe pelo menos um número
tem_oito = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_oito and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida! Requisitos: 8 caracteres e ao menos 1 número.")