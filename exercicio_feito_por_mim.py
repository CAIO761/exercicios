clientes = []

def obter_dados():
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF: ")
    rg = input("Digite seu RG: ")
    data_de_nascimento = int(input("Digite sua data de nascimento: "))
    endreco = input("Digite seu Endereço: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu Estado: ")
    telefone = int(input("Digite seu telefone: "))
    celular = int(input("Digite seu celular: "))
    email = int(input("Digite seu email: "))








def adicionar_dados(nome, cpf, rg, data_de_nascimento, endereco, cidade, estado, telefone, celular, email):
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
    clientes.append(cliente)

    return clientes


def mostrar_dados(dados_cliente):
    for cliente in dados_cliente:
        print (f"Nome Do cliente: {cliente("nome")}")
        print (f"CPF Do cliente: {cliente("cpf")}")
        print (f"RG Do cliente: {cliente("rg")}")
        print (f"data de nascimento Do cliente: {cliente("data de nascimento")}")
        print (f"Endereço Do cliente: {cliente("endereço")}")
        print (f"Cidade Do cliente: {cliente("cidade")}")
        print (f"Estado Do cliente: {cliente("estado")}")
        print (f"Email Do cliente: {cliente("email")}")
        print (f"Telefone Do cliente: {cliente("telefone")}")


def iniciar_sistema():
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
            adicionar_dados(obter_dados())
        else:
            print("Sistema finalizado")
            break


iniciar_sistema()          



