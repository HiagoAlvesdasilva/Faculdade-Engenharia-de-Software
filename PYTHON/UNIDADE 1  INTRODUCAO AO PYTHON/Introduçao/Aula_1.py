# Função para validar a nota
def validar_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve ser entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Valor inválido. Digite um número válido.")

# Menu De Boas Vindas e Captura Do Nome Do Aluno
print("Aluno Seja Bem Vindo(a)!!!")
nome = input("Por Favor Digite Seu Nome: ")

# F String
print(f"Ola {nome}")

# Solicitando as notas com validação
nota_1 = validar_nota("Por favor, Digite a Sua Nota Da Primeira Unidade: ")
nota_2 = validar_nota("Muito Bem, Agora Digite a Sua Nota Da Segunda Unidade: ")
nota_3 = validar_nota("Estamos Quase Lá! Agora, Digite a Sua Nota Da Terceira Unidade: ")
nota_4 = validar_nota("Por fim, Digite a Sua Nota Da Quarta Unidade: ")

# Somando as notas e dividindo pela quantidade de unidades para saber a média geral
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Condição para Aprovação ou Reprovação do Aluno
if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Exibindo as notas, a média e a situação do aluno
print("\nResumo do Desempenho:")
print(f"Nota 1: {nota_1}")
print(f"Nota 2: {nota_2}")
print(f"Nota 3: {nota_3}")
print(f"Nota 4: {nota_4}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
