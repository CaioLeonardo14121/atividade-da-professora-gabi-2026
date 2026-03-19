# 6. Missão Espacial – Lógica Composta
def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível abaixo do necessário"
    elif clima != "bom":
        return "Condições climáticas ruins"
    elif not sistema_ok:
        return "Erro nos sistemas"
    else:
        return "Decolagem liberada"