import json
import uuid

# Definições
tamanhoID = 10
arquivo = 'usuarios.json'

# Funções
# Cria id aleatório
def create_id():
    return str(uuid.uuid4().hex)[:tamanhoID] 

# Checka por duplicadas
def check_double_id(dados, novo_id):
    return any(usuario['_id'] == novo_id for usuario in dados['usuarios'])

# Coleta os inputs 
def get_info(dados):
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = input("Digite sua idade: ")
    curso = input("Digite seu curso: ")
    instituicao = input("Digite sua instituição: ")
    
    # Checa se check_double_id é falso
    while True:
        id = create_id
        if not check_double_id(dados, id):
            break
        
    try:
        idade = int(idade)
    except:
        print("Valor idade deve ser um número")
        return 0        
            
    return {
        
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
        'curso': curso,
        'instituição': instituicao,
        '_id': create_id()
        
    }

# Abre o arquivo e lê os valores
def read_users(arquivo):
    try:
        with open(arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    except:
        dados = {'quantidade': 0, 'usuarios': []}

    print("Dados foram lidos")
    return dados

# Escreve o usuário no arquivo
def write_users(arquivo, dados):
    try:
        with open(arquivo, 'w') as arquivo:
            # indent para quebrar linha
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)
    except:
        return 0
    
    print("Dados foram escritos.")

# Adiciona o usuário na JSON.
def add_user(dados, usuario):
    dados['usuarios'].append(usuario)
    dados['quantidade'] += 1

# Código principal
dados = read_users(arquivo)

while True:
    usuario = get_info(dados)
    if usuario == 0:
        continue
    add_user(dados, usuario)
    write_users(arquivo, dados)
    if not input("Adicionar outro usuário? (S/N): ") == 'S':
        break
    