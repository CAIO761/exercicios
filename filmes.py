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
    Filmes = dados_filme()
    Filmes.append(adicionar)
    with open(filmes, "w", encoding = "utf-8") as arq_json:
            json.dump(Filmes, arq_json, indent=4, ensure_ascii=False)

def mostrar_filme(mostrar):
    for filme in mostrar:
        print(f'''
        Nome do filme: {filme("nome")}
        Genero do filme: {filme("genero")}
        classificação: {filme("classificação")}

        ''')


def opções_escolha():
    Filmes = dados_filme()
    while True:
        print("="*80)
        print("Opção 1 -> Filme Escolhido")
        print("Opção 2 -> Cadastrar filme")
        print("Opção 3 -> Sistema finalizado")
        print("="*80)
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            mostrar_filme(Filmes)
        elif opcao == "2":
            cadastro_filmes(colocar_em_cartaz())
        elif opcao == "3":
            print("Encerrou a escolha!")
            break
        else:
            print("Não tem essa opção!. Escolha uma das acimas.")
        
opções_escolha()

            





    














