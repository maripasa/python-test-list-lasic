# Deletar Usuários

import json

arquivo_json = 'usuarios.json'

# Função que deleta o usuário
def deletar_usuario(arquivo_json, id):
    try:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print("Arquivo não pode ser aberto.")
        return None

    usuarios = dados['usuarios']

    # Busca e remove o usuário com o id dado
    for usuario in dados['usuarios']:
        if usuario['_id'] == id:
            try:
                usuarios.remove(usuario)
            except:
                print("Não pode remover usuário.")
                return None
            dados['quantidade'] -= 1
            print(f"Usuário com ID {id} removido ({usuario['nome']} {usuario['nome']}).")
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
    
# Código principal
while True:
    id_atual = input("Insira um ID: ")
    deletar_usuario(arquivo_json, id_atual)
    if not input("Deletar outro usuário? (S/N): ").upper() == 'S':
        break