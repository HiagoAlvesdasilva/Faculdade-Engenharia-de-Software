# Aplicando aula 

#Suponha que estamos gerenciando um cadastro de uma loja, e essa loja, pecisa de uma orientação em qual o publico deve investir, sendo assim, querem saber a idade media dos clientes

import pandas as pd

#Criar um dicionario com nomes e idades
dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'Dadiv', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}

#Criar Uma Serie de idades
serie_idades = pd.Series(dados['Idade'], index= dados['Nome'] )

#Exibir a Serie de idades
print("Série De Idades: ")
print(serie_idades)

#Calcular Media Das IIdades
media_idades = serie_idades.mean()
print("\nMédia de Idades: ", media_idades)





