print("Digite 5 números que voce gostaria de somar")
loop = 1
soma = 0

while loop <= 5:
    numero = int(input())
    soma += numero
    loop += 1

print(f"{soma}")
print("")