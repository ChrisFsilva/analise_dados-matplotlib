import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Carregar o arquivo

df = pd.read_csv('dados_venda.csv')

# Verificar a média das vendas
media_vendas = df ['Vendas'].mean()
print ('Media de vendas: ',media_vendas)

# Verificando maior venda
maior_venda = df.loc[df['Vendas'].idxmax()]
print ('Maior Venda: ', maior_venda)

# Verficando a menor venda
menor_venda = df.loc[df['Vendas'].idxmin()]
print (f'Menor venda: {menor_venda}')

# Grafico
plt.figure(figsize = (10,6))
sns.lineplot(x = 'Meses', y = 'Vendas', data = df, marker = 'o', linewidth = 1.5, color = 'lightgray')

# Personalização

plt.title('Analise de vendas', fontsize = 30, pad = 20)
plt.xlabel('Meses de vendas', fontsize = 12)
plt.ylabel('Vendas', fontsize = 12)
plt.grid(True, linestyle = '--', alpha = 0.7)

for i, row in df.iterrows():
    plt.text(row['Meses'], row['Vendas'], f'R${row['Vendas']}',
                ha = 'center', va = 'top', bbox = dict (facecolor = 'lightgray', alpha = 0.8), fontsize = 10,)

# Ajustar Layout para que não vaze informação para fora do grafico
plt.tight_layout()

# ajustar titulos inferiores
plt.xticks(rotation = 45)

# Salvamento automativco
plt.savefig('vendas_mes.png', dpi = 300, bbox_inches = 'tight' )

plt.show()