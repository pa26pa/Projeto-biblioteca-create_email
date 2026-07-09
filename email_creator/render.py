import json
from resources import load

class render():
    def look_types():
        data = load()
        
        types = []
        
        for template in data.values():
            types.append(template["type"])

        return types
    

    def search(name, campo):
        data = load()
        return data[name][campo]