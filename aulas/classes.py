from usuario import Usuario

print("Execução normal do arquivo...")
usuario = Usuario("Lucas", 8)
usuario2 = Usuario("Jão", 22)

print(f"objeto usuario {usuario}")
print(f"objeto usuario2 {usuario2}")

print(usuario.nome)
print(usuario.idade)

usuario.idade = 28

print(f"nova idade {usuario.idade}")
usuario.apresentar()
usuario2.apresentar()