import pandas as pd
import requests
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import scipy.stats as stats
from numpy import log10, diff
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_absolute_error, mean_squared_error

def decomposicao_serie(dataset: pd.DataFrame, frequencia_tempo: int) -> None:
    """Decomposição da série temporal para visualização dos seus componentes
       
       :param dataset: dados da série temporal a serem utilizados
       :type dataframe: pd.Dataframe
       :param frequencia_tempo: intervalo de tempo para decompor a série
       :type frequencia_tempo: int
    """
    decomposicao_serie = seasonal_decompose(dataset, period=frequencia_tempo)
    plt.figure(figsize=(30, 10))
    plt.subplot(411)
    plt.plot(dataset, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(decomposicao_serie.trend, label='Tendência')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(decomposicao_serie.seasonal, label='Sazonalidade')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(decomposicao_serie.resid, label='Residuos')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show();
    return None


def teste_normalidade(dataset: pd.DataFrame) -> None:
    """Gráfico e teste estatistico para verificar a distribuição dos dados
       da série temporal.
       
       :param dataset: dados da série temporal a serem utilizados
       :type dataframe: pd.Dataframe
    """
    dados_distribuicao = dataset['valor'].values
    plt.figure(figsize=(10, 5))
    stats.probplot(dados_distribuicao, dist='norm', plot=plt)
    plt.title('Normal QQ plot')
    plt.show();
    print('Teste de Shapiro-Wilk')
    print('Critério: Nível de significancia de 0.05 ou 5% (mais utilizado)')
    print('Se p > 0.05 (distribuição normal)')
    estatistica, valor_p = stats.shapiro(dataset)
    print(f'Estatística do teste: {estatistica}')
    print(f'Valor p: {valor_p}')
    print()
    return None


def teste_kpss(dataset: pd.DataFrame) -> None:
    """Teste estatístico para determinação da estacionariedade da série
    
       :param dataset: dados da série temporal a serem utilizados
       :type dataframe: pd.Dataframe
    """
    print('Teste de estacionariedade KPSS')
    print('H0 - Não estacionária: estatística do teste > valor crítico')
    print('HA - Estacionária: estatística do teste < valor crítico')
    teste_estacionariedade = kpss(dataset, nlags='legacy')
    print(f'Estatística do teste: {teste_estacionariedade[0]}')
    print(f'Valor p: {teste_estacionariedade[1]}')
    print(f'Número de lags: {teste_estacionariedade[2]}')
    print('Valores críticos:')
    for chave, valor in teste_estacionariedade[3].items():
        print(f'{chave} : {valor:.4f}')
    print()
    return None


def acf(dataset, numero_lags: int) -> None:
    """Função de autocorrelação de lags sequenciais da série temporal
       e/ou residuos.
       :param numero_lags: número de lags a serem utilizados
       :type numero_lags: int
    """
    plot_acf(dataset, lags=numero_lags)
    plt.show();
    return None


def pacf(dataset, numero_lags: int) -> None:
    """Função de autocorrelação parcial de lags aleatórios da série temporal
       e/ou residuos.
        
       :param numero_lags: número de lags a serem utilizados
       :type numero_lags: int
    """
    plot_pacf(dataset, lags=numero_lags, method='ywm')
    plt.show();
    return None


def teste_normalidade_residuos(dataset: pd.DataFrame) -> None:
    """Gráfico e teste estatistico para verificar a distribuição dos dados
       dos resíduos do modelo ARIMA.
       
       :param dataset: dados da série temporal a serem utilizados
       :type dataframe: pd.Dataframe
    """
    plt.figure(figsize=(10, 5))
    stats.probplot(dataset, dist='norm', plot=plt)
    plt.title('Normal QQ plot')
    plt.show()
    print('Teste de Shapiro-Wilk')
    print('Critério: Nível de significancia de 0.05 ou 5% (mais utilizado)')
    print('Se p > 0.05 (distribuição normal)')
    estatistica, valor_p = stats.shapiro(dataset)
    print(f'Estatística do teste: {estatistica}')
    print(f'Valor p: {valor_p}')
    print()
    return None


# Requisição dos dados para análise
url : str = 'https://api.bcb.gov.br/dados/serie/'
url_completo: str = f'{url}bcdata.sgs.7385/dados?formato=json'
dados_url: requests.models = requests.get(url_completo, verify=True)

if dados_url.ok:
    # Tratamento e limpeza dos dados
    dados: dict = dados_url.json()
    comerciais_leves: pd.DataFrame = pd.DataFrame.from_dict(dados)
    comerciais_leves['data'] = pd.to_datetime(comerciais_leves['data'],
                                              format='%d/%m/%Y')
    comerciais_leves['valor'] = comerciais_leves['valor'].astype(int)
    for indice, linha in comerciais_leves.iterrows():
        if linha['data'] > comerciais_leves.iloc[383, 0]:
            comerciais_leves.drop(indice, inplace=True)
    
    # Gráfico de linha da série temporal
    plt.figure(figsize=(30, 10))
    plt.title('Venda comerciais leves mensais (1990-2021)',
          fontdict={'fontsize': 25, 'fontweight':'bold'})
    plt.plot(comerciais_leves['data'], comerciais_leves['valor'],
             color='red', marker='o', label='Meses')
    plt.xlabel('Meses', fontdict={'fontsize': 25, 'fontweight':'bold'})
    plt.ylabel('Quantidade', fontdict={'fontsize': 25, 'fontweight':'bold'})
    plt.grid(True)
    plt.legend(loc='best', fontsize='medium')
    plt.show()
    
    # Criação das médias móveis
    comerciais_leves.set_index('data', inplace=True)
    media_movel = comerciais_leves.rolling(window=12)
    media_movel = media_movel.mean()
    plt.figure(figsize=(30, 10))
    plt.plot(comerciais_leves, label='Série Original')
    plt.plot(media_movel, color='red', label='Média movel anual')
    plt.legend(loc='best')
    plt.show()
    
    # Decomposição da série temporal
    comerciais_leves_st = comerciais_leves.reset_index()
    comerciais_leves_st.drop(comerciais_leves_st.index[372:384], inplace=True)
    comerciais_leves_st.set_index('data', inplace=True)
    decomposicao_serie(comerciais_leves_st, 12)
    
    # Teste de normalidade com gráfico qq-plot e teste shapiro-wilk
    teste_normalidade(comerciais_leves_st)
    
    # Teste de normalidade com gráfico qq-plot e teste shapiro-wilk
    serie_transformada = log10(comerciais_leves_st)
    teste_normalidade(serie_transformada)
    
    # Teste de estacionariedade da série temporal normalizada
    teste_kpss(serie_transformada)
    
    # Teste de estacionariedade após diferenciação de 1⁰ ordem  
    serie_diferenciada = serie_transformada['valor']
    serie_diferenciada = diff(serie_diferenciada)
    teste_kpss(serie_diferenciada)
    
    # Visualização de autocorrelação dos dados (lags) da série
    acf(serie_diferenciada, 60)
    
    # Visualização de autocorrelação parcial dos dados (lags) da série
    pacf(serie_diferenciada, 60)
    
    # Criação do melhor modelo ARIMA
    modelo_auto = auto_arima(serie_diferenciada, trace=True, stepwise=False,
                             seasonal=True, max_p=10, max_q=10,
                             max_P=4, max_Q=4, start_p=0,
                             start_q=0, start_P=0, start_Q=0,
                             m=12)
    
    # Melhor AIC para modelo ARIMA
    print(round(modelo_auto.aic(), 3))
    
    # Resumo geral do modelo criado pelo auto arima
    resultado_auto = modelo_auto.fit(serie_transformada)
    print(resultado_auto.summary())
    
    # Gráfico dos resíduos do modelo ARIMA criado
    residuos_auto = resultado_auto.resid
    plt.plot(residuos_auto())
    plt.show()
    
    # Teste Shapiro-Wilk para os resíduos
    teste_normalidade_residuos(residuos_auto())
    
    # Verificação da auto correlação dos resíduos
    acf(residuos_auto(), 60)
    
    # Verificação da auto correlação parcial dos resíduos
    pacf(residuos_auto(), 60)
    
    # Previsão de receita para o ano de 2022
    previsao_auto: pd.DataFrame = resultado_auto.predict(n_periods=24)
    previsao_escala_arima: pd.DataFrame = pd.DataFrame(10 ** previsao_auto,
                                                       columns=['Previsão_ARIMA'])
    pd.concat([comerciais_leves_st, previsao_escala_arima]).plot()
    
    # Gráfico com a previsão para o ano de 2022
    meses: list = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                   'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    plt.figure(figsize=(15, 5))
    plt.plot(meses, previsao_escala_arima.iloc[12:24],
             color='orange', marker='*')
    plt.title('Previsão venda mensal de comerciais leves (2022)',
              fontdict={'fontsize': 16, 'fontweight':'bold'})
    plt.grid(axis='y')
    plt.show();
    
    # Avaliação de performance do modelo ARIMA
    comerciais_leves: pd.DataFrame = comerciais_leves.reset_index()
    modelo_arima: pd.DataFrame = pd.concat([comerciais_leves['valor'].iloc[372:384],
                                           previsao_escala_arima.iloc[0:12]],
                                           axis=1).reset_index(drop=True)
    mae_arima: float = mean_absolute_error(modelo_arima['valor'].iloc[12:24],
                                    modelo_arima['Previsão_ARIMA'].iloc[0:12])
    rmse_arima: float = mean_squared_error(modelo_arima['valor'].iloc[12:24],
                                    modelo_arima['Previsão_ARIMA'].iloc[0:12]) ** (1/2)
    
    print(round(mae_arima, 2))
    print(round(rmse_arima, 2))    
else:
    print('Infelizmente não foi possível pegar os dados do site.')
