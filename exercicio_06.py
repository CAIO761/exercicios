def cadastrar_filme(descricao, classificacao, categoria1, categoria2, categoria3):
    lista_filmes = []
    filme = {
        "descricao": descricao,
        "classificacao": classificacao,
        "categorias": [categoria1, categoria2, categoria3],
    }
    lista_filmes.append(filme)
    return lista_filmes


print(cadastrar_filme("conclave", "16", "suspense", "misterio", "fatos reais"))