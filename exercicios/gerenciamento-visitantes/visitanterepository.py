import json
from visitante import Visitante

from constants import NOME_ARQUIVO, ENCONDING_ARQUIVO

def salvar_visitante(visitantes):
    dados = [visitante.to_dict() for visitante in visitantes]

    with open(NOME_ARQUIVO, "w", encoding=ENCONDING_ARQUIVO) as arquivo:
        json.dump(
        dados,
        arquivo,
        indent=4,
        ensure_ascii=False
        )


def carregar_visitantes():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCONDING_ARQUIVO) as json_file:
            dados = json.load(json_file)
            return [
                Visitante.from_dict(visitante)
                for visitante in dados
            ]
    except Exception:
        return []