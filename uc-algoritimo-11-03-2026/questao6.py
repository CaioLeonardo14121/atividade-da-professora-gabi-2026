idade = int(input("Digite a idade do atleta: "))

if idade < 12:
    cat = "Infantil"
elif idade < 18:
    cat = "Juvenil"
elif idade < 60:
    cat = "Adulto"
else:
    cat = "Sênior"

print(f"Categoria: {cat}. Bem-vindo à competição!")