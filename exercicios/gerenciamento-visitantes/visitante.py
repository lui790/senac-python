import json
class Visitante():
    def __init__(self, nome, data_nasc, cpf, tipo_de_ingresso, data_da_visita, numero_do_ingresso):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.tipo_de_ingresso = tipo_de_ingresso
        self.data_da_visita = data_da_visita
        self.numero_do_ingresso = numero_do_ingresso

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nasc,
            "tipo_ingresso": self.tipo_de_ingresso,
            "data_visita": self.data_da_visita,
            "numero_ingresso": self.numero_do_ingresso
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["cpf"],
            dados["data_nascimento"],
            dados["tipo_ingresso"],
            dados["data_visita"],
            dados["numero_ingresso"]
        )