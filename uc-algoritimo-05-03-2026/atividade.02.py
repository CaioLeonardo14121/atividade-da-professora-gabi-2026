import random

# Lista inicial
numeros = [91, 34, 67, 15, 82]

print("Lista original:", numeros)

# Ordem crescente
numeros.sort()
print("Lista em ordem crescente:", numeros)

# Ordem decrescente
numeros.sort(reverse=True)
print("Lista em ordem decrescente:", numeros)

# Segunda lista
numeros3 = [6, 7, 8, 9, 10]

# Embaralhar lista
random.shuffle(numeros3)
print("Lista embaralhada:", numeros3)

# Desafio
numeros4 = [12, 4, 25, 8, 19, 30]

print("\nLista do desafio:", numeros4)

# Crescente
numeros4.sort()
print("Ordem crescente:", numeros4)

# Decrescente
numeros4.sort(reverse=True)
print("Ordem decrescente:", numeros4)

# Embaralhar
random.shuffle(numeros4)
print("Lista embaralhada:", numeros4)