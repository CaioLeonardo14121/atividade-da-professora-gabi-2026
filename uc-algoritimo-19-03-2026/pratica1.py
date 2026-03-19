# 1. Sistema de Rank com Penalidade
def rank_jogador(pontos, derrotas):
    pontos_finais = pontos - (derrotas * 10)
    
    if pontos_finais < 0:
        return "Expulso"
    elif pontos_finais < 100:
        return "Iniciante"
    elif pontos_finais < 300:
        return "Intermediário"
    elif pontos_finais < 600:
        return "Avançado"
    else:
        return "Elite"


