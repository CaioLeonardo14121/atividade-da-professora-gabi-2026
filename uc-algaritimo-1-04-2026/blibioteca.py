# Dicionario para armazemar os livros:
catalogo = []

# Dicionario para armazenar os emprestimos:
emprestimosativo = {}
# Lista para armazenar o historico de transição:
historico = []

def adicionarlivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"erro: livro com codigo {codigo} já existe!")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"livro '{titulo}' adicionado com sucesso")
    return True
#---------------------------------------------------------------------------------------------------------------------------
def livro_mais_popular():
    contagem = {}

    # O código a baixo, verifica os empréstimsos:
    for emprestimo in historico:
        codigo = emprestimo["codigo"]

        if codigo in contagem:
            contagem[codigo] += 1
        else:
            contagem[codigo] = 1

    # Agora o código vai checar se existe algum empréstimo presente:
    if not contagem:
        print("nenhum empréstimo registrado.")
        return None

    # Aqui o código após percorrer por todos os dados, vai retornar o livro mais popular:
    mais_popular = max(contagem, key=contagem.get)

    livro = catalogo.get(mais_popular)

    print("livro mais popular:")
    print(f"titulo: {livro['titulo']}")
    print(f"autor: {livro['autor']}")
    print(f"emprestimos: {contagem[mais_popular]}")
    return livro


    # Dicionário para armazenar os livros (codigo como chave)
catalogo = {}

# Dicionário para armazenar empréstimos ativos
emprestimos_ativos = {}

# Lista para armazenar o histórico de empréstimos
historico = []


def adicionar_livro(codigo, titulo, autor, quantidade):
    # Verifica se o livro já existe
    if codigo in catalogo:
        print(f"Erro: livro com código {codigo} já existe!")
        return False

    # Adiciona o livro ao catálogo
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso!")
    return True


# ------------------------------------------------------------

def registrar_emprestimo(codigo):
    # Verifica se o livro existe
    if codigo not in catalogo:
        print("Livro não encontrado.")
        return False

    # Verifica se há quantidade disponível
    if catalogo[codigo]["quantidade"] <= 0:
        print("Livro indisponível.")
        return False

    # Diminui a quantidade
    catalogo[codigo]["quantidade"] -= 1

    # Registra no histórico
    historico.append({"codigo": codigo})

    print("Empréstimo realizado com sucesso!")
    return True


# ------------------------------------------------------------

def livro_mais_popular():
    contagem = {}

    # Conta quantas vezes cada livro foi emprestado
    for emprestimo in historico:
        codigo = emprestimo["codigo"]

        if codigo in contagem:
            contagem[codigo] += 1
        else:
            contagem[codigo] = 1

    # Verifica se há empréstimos
    if not contagem:
        print("Nenhum empréstimo registrado.")
        return None

    # Encontra o código mais popular
    mais_popular = max(contagem, key=contagem.get)

    livro = catalogo.get(mais_popular)

    if not livro:
        print("Livro não encontrado no catálogo.")
        return None

    print("\nLivro mais popular:")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Empréstimos: {contagem[mais_popular]}")

    return livro


# ------------------------------------------------------------
# EXEMPLO DE USO

adicionar_livro(1, "Dom Casmurro", "Machado de Assis", 3)
adicionar_livro(2, "1984", "George Orwell", 2)

registrar_emprestimo(1)
registrar_emprestimo(1)
registrar_emprestimo(2)

livro_mais_popular() 


# Dicionário para armazenar os livros (codigo como chave)
catalogo = {}

# Dicionário para armazenar empréstimos ativos
emprestimos_ativos = {}

# Lista para armazenar o histórico de empréstimos
historico = []


def adicionar_livro(codigo, titulo, autor, quantidade):
    # Verifica se o livro já existe
    if codigo in catalogo:
        print(f"Erro: livro com código {codigo} já existe!")
        return False

    # Adiciona o livro ao catálogo
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso!")
    return True


# ------------------------------------------------------------

def registrar_emprestimo(codigo):
    # Verifica se o livro existe
    if codigo not in catalogo:
        print("Livro não encontrado.")
        return False

    # Verifica se há quantidade disponível
    if catalogo[codigo]["quantidade"] <= 0:
        print("Livro indisponível.")
        return False

    # Diminui a quantidade
    catalogo[codigo]["quantidade"] -= 1

    # Registra no histórico
    historico.append({"codigo": codigo})

    print("Empréstimo realizado com sucesso!")
    return True


# ------------------------------------------------------------

def livro_mais_popular():
    contagem = {}

    # Conta quantas vezes cada livro foi emprestado
    for emprestimo in historico:
        codigo = emprestimo["codigo"]

        if codigo in contagem:
            contagem[codigo] += 1
        else:
            contagem[codigo] = 1

    # Verifica se há empréstimos
    if not contagem:
        print("Nenhum empréstimo registrado.")
        return None

    # Encontra o código mais popular
    mais_popular = max(contagem, key=contagem.get)

    livro = catalogo.get(mais_popular)

    if not livro:
        print("Livro não encontrado no catálogo.")
        return None

    print("\nLivro mais popular:")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Empréstimos: {contagem[mais_popular]}")

    return livro


# ------------------------------------------------------------
# EXEMPLO DE USO

adicionar_livro(1, "Dom Casmurro", "Machado de Assis", 3)
adicionar_livro(2, "1984", "George Orwell", 2)

registrar_emprestimo(1)
registrar_emprestimo(1)
registrar_emprestimo(2)

livro_mais_popular() c