EMAIL_CADASTRADO = "admin@email.com"
SENHA_CADASTRADA = "123456"

email_input = input("Digite o seu email ")
senha_input = input("Digite sua senha ")

if email_input == EMAIL_CADASTRADO and senha_input == SENHA_CADASTRADA:
    print("Login realizado com sucesso")
else:
    print("Conta nao encontrada")