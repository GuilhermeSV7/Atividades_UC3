# =========================
# PARTE 1 - INPUT E PRINT
# =========================
# Peça o nome do usuário
# Exemplo: nome = input("Digite seu nome: ")

# Mostre uma mensagem com o nome
# Exemplo: print("Olá", nome)

nome = input("Digite seu nome: ")
print("Olá", nome)

# =========================
# PARTE 2 - CONCATENAÇÃO
# =========================

# Crie duas variáveis: nome e sobrenome
# Junte as duas em uma frase
# Exemplo esperado: "Seu nome completo é: João Silva"

usuario = input("Digite seu nome")
sobrenome = input("Digite seu sobrenome")
print(usuario, sobrenome)

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

numero1 = int(input("Digite um numero"))
numero2 = int(input("Digite um outro numero "))
print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)


# =========================
# PARTE 4 - FOR
# =========================

# Faça um for que mostre os números de 1 até 10
# Exiba os números com print

for i in range(1, 11):
    print(i)

# =========================
# PARTE 5 - LISTA
# =========================

# Crie uma lista com 3 nomes

# Mostre todos os nomes usando um for

lista_C = ["Ana","Caio","Kaio"]
for x in lista_C:
    print(x)

# =========================
# PARTE 6 - DICIONÁRIO
# =========================

# Crie um dicionário com:
# nome, idade e cidade

# Mostre os valores com print



# =========================
# PARTE 7 - CLASSE E OBJETO
# =========================

# Crie uma classe chamada Pessoa

# Crie um construtor (_init_) com:
# nome e idade

# Crie um objeto dessa classe

# Mostre os dados com print



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
