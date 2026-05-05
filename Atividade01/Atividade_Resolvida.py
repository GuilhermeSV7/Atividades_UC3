# =========================
# PARTE 1 - INPUT E PRINT
# =========================

# Peça o nome do usuário
# Exemplo: nome = input("Digite seu nome: ")
# Mostre uma mensagem com o nome
# Exemplo: print("Olá", nome)

usuario = input("Qual seu nome?")
print ("Ola", usuario)

# =========================
# PARTE 2 - CONCATENAÇÃO
# =========================

# Crie duas variáveis: nome e sobrenome
# Junte as duas em uma frase
# Exemplo esperado: "Seu nome completo é: João Silva"

nome = input("Qual seu nome?")
sobrenome = input("Qual seu sobrenome?")
print(nome, sobrenome)

# =========================
# PARTE 3 - EQUAÇÃO MATEMÁTICA
# =========================

# Peça dois números ao usuário
# Faça as seguintes operações:
# Soma
# Subtração
# Multiplicação
# Divisão
# Mostre todos os resultados com print

numero1 = int(input("Me fale um numero"))
numero2 = int(input("Me fale um outro numero"))
print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)

# =========================
# PARTE 4 - FOR
# =========================

# Faça um for que mostre os números de 1 até 10
# Exiba os números com print

# FOR de 1 até 10

for i in range(1, 11):
    print(i)

# =========================
# PARTE 5 - LISTA
# =========================

# Crie uma lista com 3 nomes

# Mostre todos os nomes usando um for

Lista = ["Ana, Joao, Pedro"]
for x in Lista:
    print(x)

# =========================
# PARTE 6 - DICIONÁRIO
# =========================

# Crie um dicionário com:
# nome, idade e cidade

# Mostre os valores com print

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
# Crie uma classe chamada Pessoa
# Crie um construtor (__init__) com:
# nome e idade
# Crie um objeto dessa classe
# Mostre os dados com print

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Guilherme", "23")
# =========================
# PARTE 8 - DESAFIO FINAL
# =========================

# Crie um sistema simples que use TUDO:

# 1. Crie uma classe Pessoa (nome, idade)
# 2. Crie uma lista para guardar pessoas
# 3. Use um while com menu:

# 1 - Cadastrar pessoa
# 2 - Listar pessoas
# 3 - Sair

# Se escolher 1:
# - Peça nome e idade (input)
# - Crie o objeto (Pessoa)
# - Adicione na lista

# Se escolher 2:
# - Percorra a lista com for
# - Mostre os dados das pessoas

# Se escolher 3:
# - Encerrar o programa

# Dica:
# Use print para tudo
# Use if/else no menu

class People:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

ListaPessoas = []

class Sistema:
    def sistema():
        while True:
            print("\n1 - Cadastrar pessoa")
            print("2 - Listar pessoas")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            # Cadastrar pessoa
            if opcao == "1":
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))

                pessoa = Pessoa(nome, idade)  # cria objeto
                ListaPessoas.append(pessoa)  # adiciona na lista

                print("Pessoa cadastrada com sucesso!")

            # Listar pessoas
            elif opcao == "2":
                print("\nLista de pessoas:")

                for p in ListaPessoas:
                    print("Nome:", p.nome, "- Idade:", p.idade)

            # Sair
            elif opcao == "3":
                print("Encerrando sistema...")
                break

            # Opção inválida
            else:
                print("Opção inválida!")

