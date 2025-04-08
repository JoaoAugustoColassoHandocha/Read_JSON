import json, os

os.system('color 1f')

# Nome do arquivo JSON que será lido
nome_arq = 'LerJSON.json'

try:
    
    # Abre o JSON para leitura
    with open(nome_arq, 'r') as arq:
        # Carrega o conteúdo do arquivo JSON em um objeto Python
        dados = json.load(arq)
        
        # Imprime os dados lidos do JSON
        print('\nConteúdo do arquivo JSON:\n')
        print(dados)
        print('\n')
        os.system('pause')
        os.system('cls')
        
# Tratamento de exceções
except PermissionError:
    print(f'\nPermissão negada para acessar o arquivo "{nome_arq}"!\n')
    os.system('pause')
    os.system('cls')
    
except FileNotFoundError:
    print(f'\nArquivo "{nome_arq}" não encontrado!\n')
    os.system('pause')
    os.system('cls')
    
except json.JSONDecodeError as e:
    print(f'\nErro na decodificação JSON: {e}\n')
    os.system('pause')
    os.system('cls')
    
except Exception as e:
    print(f'\nOcorreu um erro inesperado: {e}\n')
    os.system('pause')
    os.system('cls')