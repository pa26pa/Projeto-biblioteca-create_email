import json

def load():
    with open("templates.json", "r", encoding="utf-8") as arquivo:
        data = json.load(arquivo)
        
    return data

def upload(data):
    with open("templates.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)