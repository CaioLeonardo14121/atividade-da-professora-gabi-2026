total_depositado = 0
qtd_transacoes = 0

while True:
    valor = float(input("Digite o valor do depósito (ou 0 para encerrar): "))
    if valor == 0:
        break
    total_depositado += valor
    qtd_transacoes += 1

print(f"\nTotal acumulado: R$ {total_depositado:.2f}")
print(f"Quantidade de transações: {qtd_transacoes}")