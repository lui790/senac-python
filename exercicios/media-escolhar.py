nome = input("Qual o nome do aluno?")
try:
    nota1 = int(input("Qual a nota dele em portugues?"))
    nota2 = int(input("Qual a nota dele em matematica?"))
    nota3 = int(input("Qual a nota dele em ingles?"))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        aprovacao = "Aprovado"
    if media < 7 and media >= 5:
        aprovacao = "Recuperação"
    if media < 5:
        aprovacao = "Reprovado"
    print(f"Nome - {nome} "
        f"Portugues - {nota1} "
        f"Matematica - {nota2} "
        f"Ingles - {nota3} "
        f"Media - {media:.2f} "
        f"{aprovacao}")
        

except Exception:
    print("Nota invalida")
