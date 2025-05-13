from exercicio_04 import somar_pares                                          
lista_alunos = []

def obter_dados():
    nome_aluno = input("Informe o nome completo: ")
    email_aluno = input("Informe o email: ")
    serie_aluno = input("Informe a serie do aluno: ")
    nota1_aluno = int(input("Informe a nota do Primeiro Bimestre: "))
    nota2_aluno = int(input("Informe a nota do Segundo Bimeste: "))
    nota3_aluno = int(input("Informe a nota do Terceiro Bimestre: "))

    return adicionar_aluno(nome_aluno, email_aluno, serie_aluno, nota1_aluno, nota2_aluno, nota3_aluno)


def adicionar_aluno(nome, email, serie, nota1= 0, nota2= 0, nota3= 0):
    notas = [nota1, nota2, nota3]
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": [nota1, nota2, nota3],
        "media": somar_pares(notas)
    }
    lista_alunos.append(aluno)

    return lista_alunos








#from = quer dizer que ele vai pegar uma funcao de outro arquivo
#toda funcao precisa de parenteses me frente dela

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome do Aluno: {aluno["nome"]}")
        print(f"Serie do aluno: {aluno["serie"]}")
        print(f"Email do aluno: {aluno["email"]}")
        print(f"Nota do aluno: {aluno["notas"]}")
        print(f"Media do aluno: {aluno["media"]}")
        
    return 
mostrar_dados_alunos(lista_alunos)




def iniciar_sistema():
    while True:
        print("=" *80)
        print("Opção 1 => Mostrar a lista de alunos Cadastrados.")
        print("Opção 2 => Cadastrar Alunos.")
        print("Opção 3 => Sair do sistema.")
        print("=" *80)
        opcao = input("Escolha uma das opcoes acima: ")

        if opcao == "1":
            mostrar_dados_alunos(lista_alunos)
        elif opcao == "2":
            obter_dados()
        else:
            print("Sistema finalizado")
            break 

iniciar_sistema()