<h1 align="center">Gráfico Matplotlib</h1>			
<br>
<h4 align="center"> 🚀 Projeto de Visualização de Dados 🚀 </h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
   * [Layout](#-layout)
   * [Como executar o projeto](#-como-executar-o-projeto)
     * [Pré-requisitos](#pré-requisitos)
     * [Funcionalidades](#funcionalidades)
   * [Tecnologias](#-tecnologias)
   * [Autor](#-autor)
   * [Licença](#-licença)
<!--te-->

## 💻 Sobre o projeto

Este projeto apresenta um gráfico de linha simples para visualizar o número de vendas ao longo dos anos utilizando a biblioteca Matplotlib do Python. O gráfico exibe os dados de vendas entre os anos de 2021 a 2026, com marcações visuais para cada ponto de dado, facilitando a análise e comparação.

O usuário pode modificar os dados de anos e vendas conforme sua necessidade para adaptar o gráfico a diferentes contextos.

## 🎨 Layout

O gráfico gerado apresenta:

- Eixo X representando os anos.
- Eixo Y representando o número de vendas.
- Marcadores circulares ("marker='o'") para destacar os pontos de dados.
- Cor verde para a linha do gráfico.
- Grade para facilitar a visualização dos valores.

<p align="center">
  <img alt="Exemplo Gráfico Matplotlib" src="https://matplotlib.org/stable/_images/sphx_glr_simple_plot_001.png" width="500"/>
  <img alt="Exemplo Gráfico Matplotlib" src="https://matplotlib.org/stable/_images/sphx_glr_bar_colors_001.png" width="500"/>
</p>

## 🚀 Como executar o projeto

### Pré-requisitos

- Python instalado (versão 3.x recomendada).
- Biblioteca Matplotlib instalada (`pip install matplotlib`).

### Execução

1. Copie o código Python do projeto.
2. Certifique-se de ter o Python e a biblioteca Matplotlib instalados.
3. Execute o script em seu ambiente Python.

#### Código exemplo:

```python
import matplotlib.pyplot as plt

ano = [2021, 2022, 2023, 2024, 2025, 2026]
vendas = [10000, 2000, 30000, 10000, 5000, 20000]

plt.plot(ano, vendas, marker='o', color='green')
plt.title('Vendas por ano')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()
```
```python
import matplotlib.pyplot as plt

medias_jose = [10,5,8,9,10,5,4]
meses = ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto']
# Variavel com padrões de cores diferentes para cada barra
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

plt.bar(meses, medias_jose, color=bar_colors)
plt.title('Medias')
plt.xlabel('jose')
plt.grid(True)
plt.show()
```
#### Funcionalidades
```bash
- Visualização clara das vendas ao longo dos anos.
- Marcadores nos pontos para facilitar a leitura.
- Configuração simples e personalizável.
- Pode ser usado como base para gráficos mais complexos.
```
## 🛠 Tecnologias
Python

Matplotlib

## 🦸🏻‍♂️ Autor
 <br>
  <sub><b><p>Christopher Silva</p></b></sub></a>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Christopher%20Silva-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chris-f-silva//)](https://www.linkedin.com/in/chris-f-silva/) 
[![Gmail Badge](https://img.shields.io/badge/-chrisspfc.silva@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:daniel.rodrigues.soarees@gmail.com)](mailto:chrisspfc.silva@gmail.com)

---

## 📝 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes. MIT

Feito por: Christopher Silva
