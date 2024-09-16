# A Linguagem Python

print("Aluno Seja Bem Vindo(a)!!!")
nome = input("Por Favor Digite Seu Nome: ")
# F String
print(f"Ola {nome}")
# Observe que Utilizamos a Funçao Float pois sem ela o Python entenderia todas as notas como Str
nota_1 = float(input("Porfavor Digite a Sua Nota Da Primeira Unidade: "))
nota_2 = float(input("Muito Bem Agora Digite a Sua Nota Da Segunda Unidade: "))
nota_3 = float(input(
    "Estamos Quase La Terminando Agora Digite A Sua Nota Da Terceira Unidade: "))
nota_4 = float(input("Porfim Digite a Sua Nota Da Quarta Unidade: "))

# somando as notas e dividindo pela quantidades de Unidades para saber a media geral
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Condiçao para Aprovaçao ou reprovaçao Do Aluno
if media >= 6:
    situacao = "Aprovado"
    print(f"parabens Voce Foi {situacao} Com Media {media}")
else:
    situacao = "Reprovado"
    print(f"Infelizmente Voce Foi {situacao} Com Media {media} ")
