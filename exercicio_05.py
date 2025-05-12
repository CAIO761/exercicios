from exercicio_04 import somar_pares                                          

def adicionar_aluno(nome, email, serie, nota1= 0, nota2= 0, nota3= 0):
    notas = [nota1, nota2, nota3]
    lista_alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": [nota1, nota2, nota3],
        "media": somar_pares(notas)
    }
    lista_alunos.append(aluno)
    return lista_alunos



print(adicionar_aluno("caio", "caio@g.com", "2TB", 5, 7, 8))

#from = quer dizer que ele vai pegar uma funcao de outro arquivo
#toda funcao precisa de parenteses me frente dela