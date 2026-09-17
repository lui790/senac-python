print("Primeira entrada de dados no python")

nome = input("Qual é o seu nome? ")

try:
    idade = int(input("Qual é sua idade? "))
    print(f"Olá, {nome}. Você tem {idade} anos.")
    if idade <= 12:
        print("É criança")
    elif idade <= 18:
        print("É adolescente")
    else:  
        print("É adulto")

except Exception:
    print("O valor da idade nao é valido")