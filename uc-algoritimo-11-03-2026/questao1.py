salario_base = 3500.00
bonus = 800.00
desconto = 250.00

salario_bruto = salario_base + bonus
salario_liquido = salario_bruto - desconto

print(f"Salário Bruto: R$ {salario_bruto:.2f} - Tipo: {type(salario_bruto)}")
print(f"Salário Líquido: R$ {salario_liquido:.2f} - Tipo: {type(salario_liquido)}")
print(f"Desconto: R$ {desconto:.2f} - Tipo: {type(desconto)}")