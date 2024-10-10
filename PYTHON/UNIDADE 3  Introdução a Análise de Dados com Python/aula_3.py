import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

 

print(df_selic.info())
print(df_selic)

#Verificar duplicidades de linhas (Passo Muito Importante), utilizando a função drop_duplicates
df_selic.drop_duplicates(keep='last', inplace=True)
#Mantém o Ultimo Registro (keep='last')
#Atrevéz do parâmetro  inplace=True, faz com que a transformação seja salva no DataFrame
#No nosso caso não existem linhas duplicadas 

#Adicionando colunas
from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic ['data_extracao']= data_extracao
df_selic ['responsavel'] = "Hiago"

print(df_selic.info())
df_selic.head()


df_selic.loc[0]

df_selic.loc[[0,20,70]]


teste = df_selic['valor'] < 0.01
print(type(teste))

print(teste)