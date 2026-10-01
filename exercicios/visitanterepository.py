import json

from constants import NOME_ARQUIVO, ENCONDING_ARQUIVO

def carregar_visitantes():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCONDING_ARQUIVO) as json_file:
            visitantes = json.load(json_file)
            return visitantes
    except Exception:
        print("fodeo")
    
def salvar_visitante(visitantes):
    with open(NOME_ARQUIVO, "w", encoding=ENCONDING_ARQUIVO) as arquivo:
        json.dump(visitantes, arquivo, indent=4)