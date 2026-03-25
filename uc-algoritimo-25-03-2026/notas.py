def analisar_notas(valores):
    total = sum(valores)
    qtd = len(valores)
    media_final = total / qtd
    nota_alta = max(valores)
    nota_baixa = min(valores)
    print(f"Soma Total: {total}")
    print(f"Média do Aluno: {media_final}")
    print(f"Maior: {nota_alta} | Menor: {nota_baixa}")

# Exemplo de teste:
analisar_notas([9, 5, 8, 10])