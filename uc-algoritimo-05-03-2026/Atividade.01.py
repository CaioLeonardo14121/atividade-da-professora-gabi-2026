numeros = [80, 20, 30, 20, 40, 90, 50]

print("Lista:", numeros)

# 1) Quantidade de elementos da lista
quantidade = len(numeros)
print("Quantidade de elementos na lista:", quantidade)

# 2) Quantas vezes o número 20 aparece
vezes_20 = numeros.count(20)
print("O número 20 aparece", vezes_20, "vezes na lista")

# 3) Posição do número 30
posicao_30 = numeros.index(30)
print("A posição do número 30 é:", posicao_30)

# Verificar se 100 está na lista
print("O número 100 está na lista?", 100 in numeros)