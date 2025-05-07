def adicionar_aluno(nome, email, serie):
    lista_alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": []
    }
    lista_alunos.append(aluno)
    return lista_alunos


print(adicionar_aluno("caio", "caio@g.com", "2TB"))