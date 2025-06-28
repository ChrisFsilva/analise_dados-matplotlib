import matplotlib.pyplot as plt

# Dados dos anos
ano = [2021, 2022, 2023, 2024, 2025, 2026]
# Dados de numero de vendas
vendas = [10000, 2000, 30000, 10000, 5000, 20000]


# criar um painel com vários graficos, definindo o tamanho
plt.figure(figsize = (20,6))
# Titulo do grafico
plt.title('Apresentação em grafico')

plt.subplot(1,2,1)
# Criar o padro do grafico, Variavel 'ano' = eixo X, variavel 'vendas' = Y, Marker = tipo de marcação no encontro das informações e color = cor dos graficos
plt.plot(ano, vendas, marker='o', color='green')
# Nome do grafico
plt.xlabel('Vendas')
# Apresentação das linhas do grafico
plt.grid(True)

medias_jose = [10,5,8,9,10,5,4]
meses = ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto']
# Variavel com padrões de cores diferentes para cada barra
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

plt.subplot(1,2,2)
plt.bar(meses, medias_jose, color=bar_colors)
plt.xlabel('jose')
plt.grid(True)


plt.show()
