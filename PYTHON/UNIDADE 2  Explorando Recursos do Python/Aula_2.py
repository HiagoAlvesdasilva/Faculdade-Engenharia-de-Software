# add(), in e remove()

# # Criando um conjunto vazio
# meu_conjunto = set()

# # Adicionando Elementos ao Conjunto
# meu_conjunto.add(10)
# meu_conjunto.add(20)
# meu_conjunto.add(30)
# # Imprimindo o conujnto
# print("Conjunto Apos Adicionar Elementos: ", meu_conjunto)
# elemento = 20
# if elemento in meu_conjunto:
#     print(f"{elemento} Está No Conjunto")
# else:
#     print(f"{elemento} Não Está No Conjunto")
# # Removendo elemento
# meu_conjunto.remove(20)
# # Imprimindo o Conjunto Atualizado
# print(f"Conjunto Apos Remover o lemento {elemento}", meu_conjunto)


# #Exemplo 1 -Criando dicionario vazio, seguido de atribuiçoes de chavves e valores
# dici_1 = {}
# dici_1  ['nome'] = "Maria"
# dici_1 ['idade'] = 25
# #Exemplo 2 -Criaçao de um dicionari com pares chave: valor
# dici_2 = {'nome': 'Maria', 'idade': 25}
# #Exemplo 3 -Criaçao de um dicionario com ema lista de tuplas representado pares cave:valor
# dici_3 = dict([('nome','Maria'),('idade', 25)])
# #Exemplo 4 - Criação de um dicionario usando a função built-in zip() e duas listas, uma para chaves e outra para valores
# dici_4 = dict(zip(['nome', 'idade'] , ['Maria', 25]))

# #Teste se Todas as constroçoes resultam em objetos iguais
# print(dici_1 == dici_2 == dici_3 == dici_4) #Deve Imprimir TRUE

# Importe e biblioteca Numpy
import numpy as np
# Criando Array Numpy de Numeros
my_array = np.array([1, 2, 3, 4, 5])
# imprimindo o array
print("Array Original")
print(my_array)

#realizando operaçoes Matematicas com o Array
squared_array = my_array ** 2 #Eleva cada elemento a quadrado
sum_of_elements = np.sum(my_array) # calcula e soma todos os elementos 
#Imprimimdo os resultados 
print("\nArray Ao Quadrado: ")
print(my_array)
print("\nSoma Dos Elementos Do Array")
print(sum_of_elements)
#Acessando  elementos dp Array
element_at_index_2 = my_array[2] # Acessa o elemento no Indice 2
print("\nElemento no Index 2: ", element_at_index_2)
