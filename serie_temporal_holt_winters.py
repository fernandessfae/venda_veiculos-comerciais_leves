import requests
import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pylab as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

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
    
    # Separação de dados para a previsão holt winters
    comerciais_leves_holt = comerciais_leves.reset_index(drop=True)
    comerciais_leves_holt.drop(comerciais_leves_holt.index[372:384], inplace=True)
    comerciais_leves_holt.set_index('data', inplace=True)
    
    # Criação do modelo de série temporal holt winters
    modelo_holt = ExponentialSmoothing(comerciais_leves_holt,
                                seasonal_periods=12,
                                trend='additive',
                                seasonal='additive',
                                use_boxcox=True).fit()
    
    #Visualização dos resíduos e métricas do modelo (AIC, AICc, BIC)
    modelo_holt.resid.plot();

    print(round(modelo_holt.aic, 3))
    print(round(modelo_holt.aicc, 3))
    print(round(modelo_holt.bic, 3))
    
    # Previsão dos proximos 24 meses
    previsao_holt: pd.Series = modelo_holt.forecast(24)
    
    # Gráficos com a série temporal + previsão (24 meses)
    plt.figure(figsize = (15, 5))
    plt.title('Previsão venda mensal de comerciais leves (2022)',
              fontdict={'fontsize': 16, 'fontweight':'bold'})
    plt.xlabel('Anos')
    plt.ylabel('Quantidade comerciais leves vendidos')
    modelo_holt.fittedvalues.plot(style='--', color='red',
                                  legend=True, label = 'Dados Originais')
    modelo_holt.forecast(24).plot(style='--', color='black',
                                  legend=True, label='Previsão')
    plt.show();
    
    plt.figure(figsize = (15, 5))
    plt.title('Venda comerciais leves mais a previsão para os próximos 24 meses',
              fontdict={'fontsize': 16, 'fontweight':'bold'})
    plt.xlabel('Meses')
    plt.ylabel('Quantidade de comerciais leves vendidos')
    modelo_holt.forecast(24).plot(style='--', marker='o', color='black',
                                  label='Previsão', legend=True, grid=True)
    plt.show();
    
    # Avaliação de performance do modelo Holt Winters
    mae_holt: float = mean_absolute_error(comerciais_leves['valor'].iloc[372:384],
                                    previsao_holt.iloc[0:12])
    rmse_holt: float = mean_squared_error(comerciais_leves['valor'].iloc[372:384],
                                    previsao_holt.iloc[0:12]) ** 1/2 
    
    print(round(mae_holt, 2))
    print(round(rmse_holt, 2))
else:
    print('Infelizmente não foi possível pegar os dados do site.')