import pandas as pd
import matplotlib.pyplot as plt


# 1. Gráfico de Pizza: Mostre a distribuição de vendas por mês.
# 2. Gráfico de Dispersão: Relacione vendas e lucro.
# 3. Gráfico de Barras: Compare vendas por mês.
# 4. Gráfico de Linha: Mostre a evolução do lucro ao longo dos meses.

dados = pd.read_csv('db.csv')

plt.figure(figsize = (20,5))
plt.title('Graficos de vendas')

# Grafico em Pizza de vendas por mês
plt.subplot(1,4,1)
graph_pizza = dados.groupby('Mês')['Vendas'].mean()
mesxvendas = graph_pizza.plot(kind='pie')
plt.xlabel('Vendas por mês')

# Grafico em scatter
graph_scatter = dados.groupby('Lucro')['Vendas'].mean().reset_index()

plt.subplot(1,4,2)
plt.scatter(graph_scatter['Lucro'], graph_scatter['Vendas'], marker='x')
plt.xlabel('Lucro')
plt.grid(axis='x')

# Grafico em linha
plt.subplot(1,4,4)
graph_line = dados.groupby('Mês', sort = False)['Lucro'].mean()
lucroxmes = graph_line.plot(kind = 'line', marker = 'o', color = 'Green')
plt.grid(True)

# Grafico em barra
plt.subplot(1,4,3)
graph_bar = dados.groupby('Mês', sort = False)['Vendas'].mean()
mesxmes = graph_bar.plot(kind = 'bar')
plt.xlabel('Vendas Mês x Mês')
colors = ('green', 'blue','purple','red','orange','yellow')
for barra, cor in zip(mesxmes.patches, colors):
    barra.set_color(cor)
plt.grid(axis='y')


plt.show()
