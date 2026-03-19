# 5. Sistema de Segurança com Múltiplas Condições
def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Acesso bloqueado"
    
    if usuario == "admin" and senha == "1234":
        return "Permissão total concedida"
    elif usuario == "admin":
        return "Senha inválida"
    else:
        return "Usuário não reconhecido"