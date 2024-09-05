# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import os

# Carregando o conjunto de dados
df = pd.read_csv('../data/planilha.csv')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Convertendo a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Agrupando os dados por mês e somando as vendas
df['Mês'] = df['Data'].dt.to_period('M')
planilha_mensal = df.groupby('Mês')['Vendas'].sum()

# Plotando as vendas mensais
plt.figure(figsize=(10, 6))
planilha_mensal.plot(kind='bar', color='skyblue')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)

# Verificando se o diretório de destino existe
output_dir = '../data'
if not os.path.exists(output_dir):
    print(f"Diretório {output_dir} não existe. Criando o diretório.")
    os.makedirs(output_dir)

# Salvando o gráfico como uma imagem
output_path = os.path.join(output_dir, 'vendas_mensais.png')
plt.savefig(output_path)
print(f"Gráfico salvo em {output_path}")
