
# A Funçao len()

# Cria uma lista de Numeros
numeros = [1, 2, 3, 4, 5]

# Usa A Funçao len Para Calcular o Comprimento Da Lista
comprimento = len(numeros)

# Ipmprime o Comprimento Da Lista
print("O Comprimento Da Lista é: ", comprimento)


#Definindo Uma Funçao Chamada 'soma'
def soma (a, b):
    resultado = a + b
    return resultado

resultado_soma = soma (5,3)
print(resultado_soma)

# Definindo Uma Funçao Chamada 'e_par'
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = 37
if e_par(numero):
    print(f"{numero} é um número par")
else:
    print(f"{numero} não é um número par")

#Funçao Lambda
soma = lambda a,b: a+b
resultado = soma(3,4)
print(resultado)

# Lista de Notas Dos Alunos
notas = [7.5, 8.0, 6.5, 1.0, 7.0]

# Funçao Regular Para Calcular a Média


def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


# Funçao Lambda Para Arrendondar Média Para Duas Casas Decimais
def arredondar_media(media): return round(media, 2)


# Calccular Media
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verifica Se Os Estudantes Foram Aprovados
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

# Resultados
print("Situaçao Das Notas: ", notas)
print("Situaçao Da Media: ", media_arredondada)
print("Situaçao Do Aluno: ", situacao)
