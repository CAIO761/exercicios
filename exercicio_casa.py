import json
import os 
db_clientes = "db_clientes.json"
#clientes = []
def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", endcoding = "utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []


clientes = carregar_dados()
print(clientes)


def obter_dados():
    nome = input("Digite seu nome completo: ")
    cpf = int(input("Digite seu CPF: "))
    rg = int(input("Digite seu RG: "))
    data_de_nascimento = (input("Digite sua data de nascimento: "))
    endereco = input("Digite seu Endereço: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu Estado: ")
    telefone = int(input("Digite seu telefone: "))
    celular = int(input("Digite seu celular: "))
    email = input("Digite seu email: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "data de nascimento": data_de_nascimento,
        "endereço": endereco,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "email": email,
    }
    return cliente 








def cadastrar_dados(adicionar_dados):
    clientes = carregar_dados()
    clientes.append(adicionar_dados)
    
    with open(db_clientes, "w", encoding = "utf-8") as arq_json:
        json.dump(clientes, arq_json, indent=4, ensure_ascii=False)





def mostrar_dados(dados_cliente):
    for cliente in dados_cliente:
        print (f"""
         Nome Do cliente: {cliente("nome")}
        CPF Do cliente: {cliente("cpf")}
        RG Do cliente: {cliente("rg")}
        data de nascimento Do cliente: {cliente("data de nascimento")}
        Endereço Do cliente: {cliente("endereço")}
        Cidade Do cliente: {cliente("cidade")}
        Estado Do cliente: {cliente("estado")}
        Email Do cliente: {cliente("email")}
        Telefone Do cliente: {cliente("telefone")}
    """)


def iniciar_sistema():
    clientes = carregar_dados()
    while True:
        print("=" *80)
        print("Opção 1 => Mostrar dados do cliente: ")
        print("Opção 2 => Fazer ficha do cliente: ")
        print("Opção 3 => sair do sistema: ")
        print("=" *80)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
             mostrar_dados(clientes)
        elif opcao == "2":
            cadastrar_dados(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado")
            break
        else:
            print("Opção invalida, escolha uma das opções no menu.")


iniciar_sistema()          



