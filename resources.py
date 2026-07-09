import json

def load():
    with open("templates.json", "r", encoding="utf-8") as arquivo:
        data = json.load(arquivo)
        
    return data