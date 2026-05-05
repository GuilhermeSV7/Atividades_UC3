# =========================
# PARTE 1 - INPUT E PRINT
# =========================

usuario = input("Qual seu nome?")
print("Ola", usuario)

# =========================
# PARTE 2 - CONCATENAÇÃO
# =========================

nome = input("Qual seu nome?")
sobrenome = input("Qual seu sobrenome?")
print("Seu nome completo é:", nome, sobrenome)

# =========================
# PARTE 3 - EQUAÇÃO MATEMÁTICA
# =========================

numero1 = int(input("Me fale um numero: "))
numero2 = int(input("Me fale um outro numero: "))
print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)

# =========================
# PARTE 4 - FOR
# =========================

for i in range(1, 11):
    print(i)

# =========================
# PARTE 5 - LISTA
# =========================

Lista = ["Ana", "Joao", "Pedro"]
for x in Lista:
    print(x)

# =========================
# PARTE 6 - DICIONÁRIO
# =========================

pessoa = {
    "nome": "Guilherme",
    "idade": 23,
    "cidade": "Brasília"
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

# =========================
# PARTE 7 - CLASSE E OBJETO
# =========================

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Guilherme", 23)
print(p1.nome)
print(p1.idade)

# =========================
# PARTE 8 - DESAFIO FINAL
# =========================

ListaPessoas = []

while True:
    print("\n1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = Pessoa(nome, idade)
        ListaPessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        print("\nLista de pessoas:")

        for p in ListaPessoas:
            print("Nome:", p.nome, "- Idade:", p.idade)

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")