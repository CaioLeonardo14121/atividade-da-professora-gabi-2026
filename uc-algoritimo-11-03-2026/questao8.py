valor = float(input("Valor da compra: R$ "))

if valor < 100:
    perc = 0
elif valor < 500:
    perc = 0.05
elif valor < 1000:
    perc = 0.10
else:
    perc = 0.15

desconto = valor * perc
total = valor - desconto

print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto ({perc*100}%): R$ {desconto:.2f}")
print(f"Valor final: R$ {total:.2f}")