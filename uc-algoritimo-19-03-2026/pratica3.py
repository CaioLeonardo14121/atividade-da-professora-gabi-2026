# 3. Sistema de Magia com Combinação
def tipo_magia(fogo, agua):
    if fogo and agua:
        return "Névoa"
    elif fogo:
        return "Chamas"
    elif agua:
        return "Correnteza"
    else:
        return "Sem poder"


