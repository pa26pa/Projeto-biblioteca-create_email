import json

def load():
    try:
        with open('seu_arquivo.json', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo: 
                return {}
            return json.loads(conteudo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Aviso: O arquivo JSON estava vazio ou inválido. Retornando estrutura vazia.")
        return {}

def upload(data):
    with open("templates.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)