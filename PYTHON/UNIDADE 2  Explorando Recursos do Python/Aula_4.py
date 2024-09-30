# Primeiro modo
import math

print(math.sqrt(25))

# Segundo modo
import math as m

print(m.sqrt(9))

# Criando Grafico de Linha
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Cria um Grafico de linha
plt.plot(x, y)

# Adiciona rotolos aos eixos
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adiciona um Titulo ao grafico
plt.title('Eixi De Grafico De Linha')

# Mostra o Grafico
plt.show()

# Criando Grafico de Barras
import matplotlib.pyplot as plt

# Dados de exemplo
meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI']
vendas = [120, 90, 150, 80, 200]

# Cria Um Grafico de Barras
plt.bar(meses, vendas, color='royalblue')

# Adiciona Rotulos aos Eixos
plt.xlabel('Mês')
plt.ylabel('Vendas (em Unidades)')

# Mostrar o Grafico
plt.show()
