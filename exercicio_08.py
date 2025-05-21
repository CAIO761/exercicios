import json
import os
funcio = "funcionarios.json"

def carregar_dados():
    if os.path.exists(funcio):
        with open(funcio, "r", encoding= "utf-8",) as arq_json:
            return json.load(arq_json)
    else:
        return []

funcionarios = carregar_dados()

for funcionario in funcionarios:
    if funcionario ["salario"] >= 5500:
        print(f"Nome: {funcionario ["nome"]} | Salario: {funcionario ["salario"]}")
    else:
        print("Funcionarios não encontrados")

#with vai abrir e fechar o arquivo com segurança ou manipular o arquivo com segurança
#encoding = "utf-8" ele vai colcar as regras de acordo com a lingua como as acentuações
# OS ele vai dar acesso para nós manipular os arquivos 
