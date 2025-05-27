import json
import os
filmes = "filmes.json"

def dados_filme():
    if os.path.exists(filmes):
        with open(filmes, "r", encoding= "utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def colocar_em_cartaz():
    Nome = input("Nome do filme: ")
    Genero = input("Genero do filme: ")
    classificacao = input("Classificação indicativa: ")

    filme = {
        "nome": Nome,
        "genero": Genero,
        "classificação": classificacao,
    }
    return filme

def cadastro_filmes(adicionar):
    print(adicionar)
    db_filmes = dados_filme()
    db_filmes.append(adicionar)
    with open(filmes, "w", encoding = "utf-8") as arq_json:
            json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False)
#json.dump vai armazenar os dados dentro do arquivo

def mostrar_filme(filmes):
    if filmes:
        for filme in filmes:
            print(f'''
            Nome do filme: {filme["nome"]}
            Genero do filme: {filme["genero"]}
            classificação: {filme["classificação"]}

            ''')
    else:
        print("Não existe nenhum filme cadastrado!")


def iniciar_sistema():
    db_filmes = dados_filme()
    while True:
        print("="*80)
        print("Opção 1 -> Filme Escolhido")
        print("Opção 2 -> Cadastrar filme")
        print("Opção 3 -> Sistema finalizado")
        print("="*80)
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            mostrar_filme(db_filmes)
        elif opcao == "2":
            cadastro_filmes(colocar_em_cartaz())
        elif opcao == "3":
            print("Encerrou a escolha!")
            break
        else:
            print("Não tem essa opção!. Escolha uma das acimas.")
        
iniciar_sistema()





