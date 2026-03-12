def exibir_operacoes(n1, n2):
    soma = n1 + n2
    produto = n1 * n2
    
    print(f"\n--- Resultados ---")
    print(f"A soma de {n1} + {n2} é: {soma}")
    print(f"O produto de {n1} x {n2} é: {produto}")

# Interação com o usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

exibir_operacoes(num1, num2)