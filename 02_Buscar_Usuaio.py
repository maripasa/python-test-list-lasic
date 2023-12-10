# Buscar usuário

import json

arquivo_json = 'usuarios.json'

# Função que permuta pelo json buscando id
def buscar_usuario(arquivo_json, id):
    try:
        with open(arquivo_json, 'r') as arquivo:
            dados_usuarios = json.load(arquivo)

    except:
        print("Arquivo não pode ser aberto.")
        return None

    # Busca pelo usuario
    for usuario in dados_usuarios['usuarios']:
        if usuario['_id'] == id:
            return usuario
    print("Valor não encontrado.")
    return None
    
# Código principal
while True:
    id_atual = input("Insira um ID: ")
    if id_atual == None:
        break
    usuario_atual = buscar_usuario(arquivo_json, id_atual)
    print(usuario_atual)
    
    if not input("Buscar outro usuário? (S/N): ").upper() == 'S':
        break