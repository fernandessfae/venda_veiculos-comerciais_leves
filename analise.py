import requests
import pandas as pd
import seaborn as sns
import copy
import matplotlib.pyplot as plt
import scipy.stats as stats

# Requisição dos dados para análise
url : str = 'https://api.bcb.gov.br/dados/serie/'
url_completo: str = f'{url}bcdata.sgs.7385/dados?formato=json'
dados_url: requests.models = requests.get(url_completo, verify=True)

if dados_url.ok:
    # Tratamento e limpeza dos dados
    dados: dict = dados_url.json()
    comerciais_leves: pd.DataFrame = pd.DataFrame.from_dict(dados)
    comerciais_leves['valor'] = comerciais_leves['valor'].astype(int)
    comerciais_leves['data'] = pd.to_datetime(comerciais_leves['data'],
                                              format='%d/%m/%Y')
    for indice, linha in comerciais_leves.iterrows():
        if linha['data'] > comerciais_leves.iloc[383, 0]:
            comerciais_leves.drop(indice, inplace=True)
    
    # Gráfico de frequências (histograma) das vendas
    plt.figure(figsize=(10, 5))
    plt.hist(comerciais_leves['valor'], 16, rwidth=0.9, color='red')
    plt.title('Gráfico de frequência das vendas comerciais leves (1990-2021)',
              fontdict={'fontsize': 16, 'fontweight':'bold'})
    plt.show()
    
    # Medidas de tendência central
    print(f'Media das vendas: {round(comerciais_leves["valor"].mean(),2)}')
    print(f'Mediana das vendas: {round(comerciais_leves["valor"].median(),2)}')
    print(f'Moda da vendas: {round(comerciais_leves["valor"].mode(),2)}\n')
    
    # Medidas de dispersão (em relação a média)
    print(f'Variância das vendas: {round(comerciais_leves["valor"].var(),2)}')
    print(f'Desvio padrão das vendas: {round(comerciais_leves["valor"].std(),2)}\n')
    
    # Medidas de posição
    print(round(comerciais_leves['valor'].describe()), 2)
    
    # Boxplot valores mensais
    plt.figure(figsize=(15, 5))
    plt.boxplot(comerciais_leves['valor'], vert=False,
                flierprops=dict(marker='o', markerfacecolor='red',
                                markersize=12, linestyle='none'))
    plt.title('Gráfico de caixa vendas mensais comerciais leves (1990-2021)',
              fontdict={'fontsize': 16, 'fontweight':'bold'})
    plt.show()
        
    # Visualização dos outliers do boxplot no gráfico de barras
    valor_maximo: float = comerciais_leves['valor'].quantile(q=0.75) + 1.5 * \
        (comerciais_leves['valor'].quantile(q=0.75) - \
         comerciais_leves['valor'].quantile(q=0.25))
    
    outliers: pd.DataFrame = copy.deepcopy(comerciais_leves)
    outliers = outliers.loc[outliers['valor'] > valor_maximo]
    outliers['data'] = outliers['data'].dt.strftime('%Y/%m/%d')
    plt.figure(figsize=(20, 5))
    colors: list = ['#FF2400', '#FF664D', '#FF664D', '#FF664D', '#FF664D',
                    '#FF664D', '#FF664D', '#FF664D', '#FF664D', '#FFA799',
                    '#FFA799', '#FFA799', '#FFA799', '#FFA799', '#FFA799',
                    '#FFA799', '#FFA799', '#FFA799', '#FFE9E5', '#FFE9E5',
                    '#FFE9E5', '#FFE9E5', '#FFE9E5', '#FFE9E5', '#FFE9E5',
                    '#FFE9E5', '#FFE9E5', '#FFE9E5']
    plt.bar(outliers['data'], outliers['valor'], color=colors)
    plt.title('Visualização outliers comerciais leves (1990-2021)',
              fontdict={'fontsize': 16, 'fontweight':'bold'})
    plt.xticks(rotation='vertical')
    plt.show()
    
    # Medidas de posição e boxplot anual dos outliers, exceto 2010
    outliers_anual: pd.DataFrame = copy.deepcopy(outliers)
    outliers_anual.drop([251], inplace=True)
    outliers_anual['data'] = outliers_anual['data'].str[0:4].astype(int)
    print(round(outliers_anual.groupby('data').describe(), 2))
    #print(outliers_anual.groupby('data').sum())
    outliers_anual.boxplot(figsize=(10, 5), by='data')
    
    # Gráfico boxplot anual
    boxplot_anual: pd.DataFrame = copy.deepcopy(comerciais_leves)
    boxplot_anual['data'] = boxplot_anual['data'].dt.strftime('%Y/%m/%d')
    boxplot_anual['data'] = boxplot_anual['data'].str[0:4].astype(int)
    print(round(boxplot_anual.groupby('data').describe(), 2))
    boxplot_anual.boxplot(figsize=(30, 10), by='data')
    plt.show()
    
    # Teste de normalidade vendas mensais periodo com histograma
    sns.histplot(comerciais_leves['valor'], bins=16, color='red',
                 kde=True, stat='probability')
    
    # Teste shapiro-wilk vendas mensais periodo
    print('Teste de Shapiro-Wilk')
    print('Critério: Nível de significancia de 0.05 ou 5% (mais utilizado)')
    print('Se p > 0.05 (distribuição normal)')
    estatistica, valor_p = stats.shapiro(comerciais_leves['valor'])
    print(f'Estatistica do teste: {estatistica}')
    print(f'Valor p: {valor_p}')      
else:
    print('Infelizmente não foi possível pegar os dados do site.')
    