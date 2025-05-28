import json
import os
agenda_salao = "agenda cabeleleiro.json"

def carregar_dados():
    if os.path.exists(agenda_salao):
        with open(agenda_salao, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
barbeiro = carregar_dados()

def obter_dados():
    nome_do_cliente = input("Digite seu nome por favor: ")
    serviço_escolhido = input("Digite o serviço que deseja fazer?: ")
    data = input("Qual a data que deseja?: ")
    horario = input("O horario que gostaria?: ")
    observação = input("Algo que tenha alergia ou queira em especifico?: ")    
    
    salao = {
        "nome": nome_do_cliente,
        "servico": serviço_escolhido,
        "data": data,
        "horario": horario,
        "observação": observação
    }
    return salao


def cadastrar_agendamento(receber_agenda):
    barbeiro.append(receber_agenda)
    with open(agenda_salao, "w", encoding="utf-8") as arq_json:
        json.dump(barbeiro, arq_json, indent=4, ensure_ascii= False)


def mostrar_agendamento(agenda_salao):
    if agenda_salao:
        for salao in agenda_salao:
            print(f'''
            Nome do cliente: {salao["nome"]}
            Serviço do cliente: {salao["servico"]}
            Data do cliente: {salao["data"]}
            Horario do cliente: {salao["horario"]}
            Observação do cliente: {salao["observação"]}

              ''')
    else:
        print("Não tem um agendamento no sistema!")


def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 -> Mostrar agenda completa!")
        print("Opção 2 -> Cadastrar novo agendamento")
        print("Opção 3 -> Sair do sistema!")
        print("="*80)
        opcao = input("Escolha uma opção acima: ")

        if opcao == "1":
            mostrar_agendamento(barbeiro)
        elif opcao == "2":
            cadastrar_agendamento(obter_dados())
        elif opcao == "3":
            print("Saiu do sistema com sucesso!")
            break
        else:
            print('''
                  A opção que você escolheu não está disponivel!. 
                  Escolha uma das opções acima
                  ''')
            
iniciar_sistema()