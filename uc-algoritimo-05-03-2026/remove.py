nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print("nomes: ", nomes )

nomes.remove("Bruno")
print("Lista atualizada", nomes)

#removido = nomes. pop()
removido = nomes.pop(1)
print(f"Removido: {removido}")
print("após pop():",nomes)

# del - remover pelo indice 
del nomes[0]
print("após del nomes[0]", nomes)

# clear: esvazia
nomes.clear()
print("Lista atualizada: ", nomes)
