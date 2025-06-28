import matplotlib.pyplot as plt

# Dados dos anos
ano = [2021, 2022, 2023, 2024, 2025, 2026]
# Dados de numero de vendas
vendas = [10000, 2000, 30000, 10000, 5000, 20000]

# Criar o padro do grafico, Variavel 'ano' = eixo X, variavel 'vendas' = Y, Marker = tipo de marcação no encontro das informações e color = cor dos graficos
plt.plot(ano, vendas, marker='o', color='green')
# Titulo do painel grafico
plt.title('Vendas por ano')
# Nome do grafico
plt.xlabel('Vendas')
#plt.grid(True)
plt.show()