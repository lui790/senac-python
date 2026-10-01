# def saudacao():
#     print("Olá, mundo")

# saudacao()

# def saudacao_com_nome(nome="Aluno"):
#     print(f"Olá, meu nome é {nome}")

# saudacao_com_nome("Luis")
# saudacao_com_nome("seu zé")
# saudacao_com_nome()

# def somar(a, b):
#     soma = a + b 
#     return soma

# print(somar(5, 2))


def cadastrar_usuario(nome: str, idade: int = 18):
    print(f"Cadastrando nome {nome} {type(nome)}")
    print(f"Cadastrando Idade {idade} {type(idade)}")

cadastrar_usuario("Luis", 19)
cadastrar_usuario("Maria")

cadastrar_usuario(nome="Ikaro", idade=46)
cadastrar_usuario(idade=40, nome="Zec")
# cadastrar_usuario(idade=40, "Marlene") dá erro
cadastrar_usuario("Marlene", idade=40)
cadastrar_usuario(10, "texto")