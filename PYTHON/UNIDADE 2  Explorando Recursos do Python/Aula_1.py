texto = "Explorando a Diversidade de Linguagens de Programação com Python."

print(f"tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in (texto)}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As 10 primeiras Letras São {texto[:10]}")

# Listas
cores = ['vermelho', 'azul', ' verde', 'amarelo', 'roxo']
for cor in cores:
    print(f'Posição = {cores.index(cor)}, cor = {cor}')


# ------
linguagens = ["Python", "Java", "JavaScript",
              "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("Antes da Listagem = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print(f"\nDepois da Listagem = ", linguagens)


#Funçao MAP
#Aplica a uma Funçao em toda sequancia
#map (função, sequancia)
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
preco_em_reais = list (map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(preco_em_reais)


#Função filter
#filtra os elementos de uma sequencia com base em uma funçao de teste(retorna true ou false)
#filter (funçao_teste, sequancia)
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)