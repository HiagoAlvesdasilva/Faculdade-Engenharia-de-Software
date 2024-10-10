#Aplicando Aula

#Suponha, agora que você trabalha em uma loja de itens variados, 
#por conta de um erro no sistema de venda, não mostra o valor unitário dos itens vendidos,e existem algumas duplicações de linhas. 
#Você precisa mostrar itens com valores acima de R$50.00 para oplanejamento da empresa em uma ação de Marketing 

import pandas as pd

#Criando um DataFrame com 5 linhas de dados 
data = {
    'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],
    'quantidade de itens comprados': [3,1,4,3,2],
    'tipo de item': ['Eletrônico', 'Vestuario', 'Alimento', 'Eletronico', 'Alimento'],
    'receita total': [120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)
print(df)


# Removendo duplicatas, mantendo a última ocorrência de cada item
df.drop_duplicates(subset='nome', keep='last', inplace=True)
print(df)


#Calculando a coluna "preco do item "

df['preco do item'] = df['receita total'] / df['quantidade de itens comprados']

itens_acima_de_50 = df[df['preco do item'] > 50]

print("Itens Acima De 50R$: ")
print(itens_acima_de_50)

