def calcularSalario(valor_hora, horas_trabalhadas):
    total = valor_hora * horas_trabalhadas
    return total

# Simulando uma entrada de dados
print("### Sistema de Folha de Pagamento ###")
valor_por_hora = float(input("Quanto você ganha por hora? R$ "))
horas_mes = float(input("Quantas horas você trabalhou este mês? "))

# Chamada da função e armazenamento do resultado
salario_final = calcularSalario(valor_por_hora, horas_mes)

print(f"\nObrigado pelas informações!")
print(f"Seu salário total este mês é de: R$ {salario_final:,.2f}")
