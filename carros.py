import json
import os
cadastro_veiculos = "cadastro dos veiculos.json"

def carregar_dados():
    if os.path.exists(cadastro_veiculos):
        with open(cadastro_veiculos, "r", encoding= "utf-8") as arq_json:
           return json.load(arq_json)
    else:
        return []
    
carro = carregar_dados()

def obter_dados():
    marca_do_veiculo = input("Digite a marca do veiculo por favor: ")
    modelo_do_veiculo = input("Digite o modelo do veiculo por favor: ")
    ano_de_fabricação = int(input("Digite o ano de frabricação por favor: "))
    cor_do_veiculo = input("Digite a cor do veiculo por favor: ")

    carros = {
        "marca_do_veiculo": marca_do_veiculo,
        "modelo_do_veiculo": modelo_do_veiculo,
        "ano_de_fabricação": ano_de_fabricação,
        "cor_do_veiculo": cor_do_veiculo
    }
    return carros



def cadastro_carro(receber_dados_carro):
    carro.append(receber_dados_carro)
    with open(cadastro_veiculos, "w", encoding= "utf-8",) as arq_json:
        json.dump(carro, arq_json, indent=4, ensure_ascii=False)


def dados_carro(cadastro_veiculos):
    if cadastro_veiculos:
        for carros in cadastro_veiculos:
            print(f'''
            Marca do carro: {carros["marca_do_veiculo"]}
            Modelo do carro: {carros["modelo_do_veiculo"]}
            Ano do carro: {carros["ano_de_fabricação"]}
            Cor do carro: {carros["cor_do_veiculo"]}
            ''')
    else:
        print("Não existe esse veiculo cadastrado!")


def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 -> Carro cadastrado!")
        print("Opção 2 -> Cadastrar carro?")
        print("Opção 3 -> Sair do sistema!")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")

        if opcao == "1":
            dados_carro(carro)
        elif opcao == "2":
            cadastro_carro(obter_dados())
        elif opcao == "3":
            print("Encerrou o sistema!")
            break
        else:
         print("A opção que você escolheu não existe. Por favor escolha uma das opções acima")

iniciar_sistema()




