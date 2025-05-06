
def informacao_pessoal(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade"
    else:
        return f"{idade} é menor de idade"

print (informacao_pessoal("Caio", 18))    