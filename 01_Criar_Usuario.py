# Criar usuário

import json
import uuid

# Definições
tamanhoID = 10
arquivo_json = 'usuarios.json'

# Funções

# Cria id aleatório
def criar_id():
    return str(uuid.uuid4().hex)[:tamanhoID] 

# Checa por duplicatas de ID
def tem_id_duplicado(dados, novo_id):
    return any(usuario['_id'] == novo_id for usuario in dados['usuarios'])

# Coleta os inputs e cria um novo usuário
def obter_info(dados):
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = input("Digite sua idade: ")
    curso = input("Digite seu curso: ")
    instituicao = input("Digite sua instituição: ")
    
    # Checa se tem_id_duplicado é falso
    while True:
        novo_id = criar_id()
        if not tem_id_duplicado(dados, novo_id):
            break
        
    try:
        idade = int(idade)
    except ValueError:
        print("Valor idade deve ser um número")
        return None
    print(f"Novo ID: {novo_id}")     
            
    return {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
        'curso': curso,
        'instituição': instituicao,
        '_id': novo_id
    }

# Abre o arquivo e lê os valores
def ler_usuarios(arquivo_json):
    try:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
            
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Inicializando novo.")
        dados = {'quantidade': 0, 'usuarios': []}
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Inicializando novo.")
        dados = {'quantidade': 0, 'usuarios': []}

    print("Dados foram lidos")
    return dados

# Adiciona o usuário na JSON.
def adicionar_usuario(dados, usuario):
    dados['usuarios'].append(usuario)
    dados['quantidade'] += 1

# Escreve o usuário no arquivo
def escrever_usuario(arquivo_json, dados):
    try:
        with open(arquivo_json, 'w') as arquivo:
            # indent para quebrar linha
            json.dump(dados, arquivo, indent=2)
    except:
        print("Dados NÃO foram escritos.")
        return None
    
    print("Dados foram escritos.")

# Código principal
dados = ler_usuarios(arquivo_json)

while True:
    usuario = obter_info(dados)
    if usuario == {'quantidade': 0, 'usuarios': []}:
        break
    if usuario == None:
        continue
    adicionar_usuario(dados, usuario)
    escrever_usuario(arquivo_json, dados)
    if not input("Adicionar outro usuário? (S/N): ").upper() == 'S':
        break
    