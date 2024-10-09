import pandas as pd

#Criando uma lista de valores
exemplo1 = [10,20,30,40,50]

#Criando uma Series atravez de lista
series1 = pd.Series(data = exemplo1)

print (series1)
print (exemplo1)


import pandas as pd

#Criando um dicionario com pares chave-valor
Exemplo2 = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

#Criando uma Series apartir de um dicionario 
Series2 = pd.Series(data=Exemplo2)
print(Series2)
print(Exemplo2)


import pandas as pd
url = 'https://www.fdic.gov/bank-failures/failed-bank-list'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)

print(df_bancos.dtypes)