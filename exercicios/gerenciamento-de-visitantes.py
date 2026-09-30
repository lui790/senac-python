import uuid
import json

from datetime import datetime

loop = True

visitantes = []

def solicitar_texto(mensagem):

    while True:

        valor = input(mensagem).strip()
        if valor != "":
            return valor

        print("Este campo não pode ficar vazio.")

def calcular_idade(data_nascimento):

    data_nascimento = datetime.strptime(
        data_nascimento,
        "%d/%m/%Y"
    )

    hoje = datetime.now()

    idade = hoje.year - data_nascimento.year

    if (
        hoje.month,
        hoje.day
    ) < (
        data_nascimento.month,
        data_nascimento.day
    ):

        idade -= 1

    return idade


def cpf_cadastrado(visitantes, cpf):

    for visitante in visitantes:

        if visitante["cpf"] == cpf:

            return True

    return False

def cadastrar_visitante(visitantes):

    print("\n" + "=" * 50)
    print("CADASTRO DE VISITANTE")
    print("=" * 50)

    nome = solicitar_texto("Nome: ")

    while True:

        data_nascimento = solicitar_texto(
            "Data de nascimento (DD/MM/AAAA): "
        )

        try:
            datetime.strptime(
                data_nascimento,
                "%d/%m/%Y"
            )

            break

        except ValueError:

            print(
                "Data invalida. "
                "Use o formato DD/MM/AAAA."
            )

    while True:

        cpf = solicitar_texto("CPF: ")
        if cpf_cadastrado(visitantes, cpf):

            print(
                "Este CPF ja esta cadastrado."
            )

        else:

            break


    print("\nTipos de ingresso:")
    print("1 - Normal")
    print("2 - VIP")
    print("3 - Premium")

    while True:

        tipo_opcao = input(
            "Escolha o tipo de ingresso: "
        ).strip()

        if tipo_opcao == "1":

            tipo_ingresso = "Normal"
            break

        elif tipo_opcao == "2":

            tipo_ingresso = "VIP"
            break

        elif tipo_opcao == "3":

            tipo_ingresso = "Premium"
            break

        else:

            print(
                "Opção invalida. "
                "Escolha 1, 2 ou 3."
            )


    while True:

        data_visita = solicitar_texto(
            "Data da visita (DD/MM/AAAA): "
        )

        try:
            datetime.strptime(
                data_visita,
                "%d/%m/%Y"
            )

            break

        except ValueError:

            print(
                "Data invalida. "
                "Use o formato DD/MM/AAAA."
            )

    numero_ingresso = str(uuid.uuid4())

    visitante = {

        "nome": nome,

        "data_nascimento": data_nascimento,

        "cpf": cpf,

        "tipo_ingresso": tipo_ingresso,

        "data_visita": data_visita,

        "numero_ingresso": numero_ingresso
    }

    visitantes.append(visitante)

    print("\nVisitante cadastrado com sucesso!")

    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Tipo de ingresso: {tipo_ingresso}")
    print(f"Data da visita: {data_visita}")
    print(f"Numero do ingresso: {numero_ingresso}")

    with open("visitantes.json", "w", encoding="utf-8") as json_file:
    json.dump(visitantes, json_file, ensure_ascii=False, indent=4)

    print("Salvo com sucesso")

def listar_visitantes(visitantes):

    print("\n" + "=" * 70)
    print("LISTA DE VISITANTES")
    print("=" * 70)

    if len(visitantes) == 0:

        print("Nenhum visitante cadastrado.")

        return


    for indice, visitante in enumerate(visitantes, start=1):

        idade = calcular_idade(
            visitante["data_nascimento"]
        )

        print(f"\nVisitante {indice}")
        print(f"Nome: {visitante['nome']}")
        print(f"Idade: {idade} anos")
        print(
            f"Tipo de ingresso: "
            f"{visitante['tipo_ingresso']}"
        )

def consultar_visitante(visitantes):

    print("\n" + "=" * 50)
    print("CONSULTAR VISITANTE")
    print("=" * 50)

    cpf = solicitar_texto(
        "Digite o CPF do visitante: "
    )

    for visitante in visitantes:

        if visitante["cpf"] == cpf:

            idade = calcular_idade(
                visitante["data_nascimento"]
            )

            print("\nVisitante encontrado!")

            print("-" * 50)

            print(f"Nome: {visitante['nome']}")

            print(
                f"Data de nascimento: "
                f"{visitante['data_nascimento']}"
            )

            print(f"Idade: {idade} anos")

            print(f"CPF: {visitante['cpf']}")

            print(
                f"Tipo de ingresso: "
                f"{visitante['tipo_ingresso']}"
            )

            print(
                f"Data da visita: "
                f"{visitante['data_visita']}"
            )

            print(
                f"Numero do ingresso: "
                f"{visitante['numero_ingresso']}"
            )

            print("-" * 50)
            return

    print(
        "\nNenhum visitante encontrado "
        "com esse CPF."
    )

def remover_visitante(visitantes):

    print("\n" + "=" * 50)
    print("REMOVER VISITANTE")
    print("=" * 50)

    cpf = solicitar_texto(
        "Digite o CPF do visitante: "
    )

    for visitante in visitantes:

        if visitante["cpf"] == cpf:
            print(
                f"\nVisitante encontrado: "
                f"{visitante['nome']}"
            )

            confirmar = input(
                "Deseja realmente remover? (S/N): "
            ).strip().upper()


            if confirmar == "S":
                visitantes.remove(visitante)

                print(
                    "\nVisitante removido com sucesso!"
                )

            else:

                print(
                    "\nOperação cancelada."
                )

            return



    print(
        "\nNenhum visitante encontrado "
        "com esse CPF."
    )

def main():

    visitantes = carregar_visitantes()

    while True:

        print("\n" + "=" * 60)
        print("CENTRAL DE VISITANTES DO PARQUE")
        print("=" * 60)

        print("1 - Cadastrar visitante")
        print("2 - Remover visitante")
        print("3 - Listar visitantes")
        print("6 - Consultar visitante")
        print("0 - Encerrar programa")

        print("=" * 60)


        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":

            cadastrar_visitante(visitantes)


        elif opcao == "2":

            remover_visitante(visitantes)


        elif opcao == "3":

            listar_visitantes(visitantes)


        elif opcao == "6":

            consultar_visitante(visitantes)


        elif opcao == "0":

            print(
                "\nPrograma encerrado."
            )

            break


        else:

            print(
                "\nOpção invalida. "
                "Tente novamente."
            )

def carregar_visitantes():

    try:

        with open("visitantes.json", "r", encoding="utf-8") as json_file:

            visitantes = json.load(json_file)

            return visitantes

    except FileNotFoundError:

        return []

if loop == True:
    main()
