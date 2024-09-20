# Estruturas Condicionais em Python

# Máquina de Vendas de Ingressos Virtual

# Solicita o Nome
nome = input("Olá, seja bem-vindo(a)! Por favor, digite seu nome: ")

# Solicita a Idade
idade = int(input(f"Muito bem, {nome}. Agora digite a sua idade: "))

# Verifica a Idade para a Sugestão de Filmes
if idade < 12:
    print("Recomendamos Filme Infantil: FILME1")
elif 12 <= idade < 18:
    print("Recomendamos Filme Adolescente: FILME2")
else:
    print("Recomendamos Filme de Ação: FILME3")

# Verificando Ingressos
quantidade_ingresso = 10
escolha = int(
    input("Escolha a quantidade de ingressos que você deseja comprar: "))

if 1 <= escolha <= 10:
    print(f"Muito bem! Você adquiriu {escolha} ingressos. Bom filme!")
else:
    print("Quantidade de ingressos não disponível. Você pode comprar de 1 a 10 ingressos.")
