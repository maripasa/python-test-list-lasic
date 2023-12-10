# Editar usuário

import json

arquivo_json = 'usuarios.json'
    
def editar_usuario(arquivo_json, id):
    try:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print("Arquivo não pode ser aberto.")
        return None

    usuarios = dados['usuarios']

    for usuario in dados['usuarios']:
        if usuario['_id'] == id:
            print(f"Nome atual: {usuario['nome']}\nSobrenome atual: {usuario['sobrenome']}\n")
            usuario['nome'] = input("Insira novo Nome: ")
            usuario['sobrenome'] = input("Insira novo Sobrenome: ")
            break
    else:
        print(f"Usuário com ID {id} não encontrado.")
        return None
    
    try:
        with open(arquivo_json, 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
        print("Dados foram atualizados no arquivo.")
        
    except:
        print(f"Erro ao escrever dados no arquivo.")
    
while True:
    id_atual = input("Insira um ID: ")
    editar_usuario(arquivo_json, id_atual)
    if not input("Editar outro usuário? (S/N): ").upper() == 'S':
        break