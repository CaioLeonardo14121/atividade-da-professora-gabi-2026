import random

numeros = [45, 12, 78, 23, 56]
print("Lista original: ", numeros)

# sort cresente 
numeros.sort()
print("Após sort(): ", numeros)

# sort decresente 
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

#  embaralha
random.shuffle(numeros)
print("Lista embaralhada: ", numeros)

