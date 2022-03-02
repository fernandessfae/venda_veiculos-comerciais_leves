# Venda de veículos comerciais leves

- Introdução
- Análise geral
  - 1. Histograma
  - 2. Medidas de tendência central
        - 2.1 Média
        - 2.2 Mediana
        - 2.3 Moda
  - 3. Medidas de dispersão
        - 3.1 Variância
        - 3.2 Desvio padrão
  - 4. Medidas de posição
        - 4.1 Quartis
  - 5. Outliers
  - 6. Teste de normalidade
        - 6.1 Histograma com linha de distribuição
        - 6.2 Teste Shapiro-Wilk
- Série temporal
  - 1. Definição
  - 2. Média móvel
  - 3. Decomposição da série temporal
  - 4. Modelagem do dados
        - 4.1 Normalidade e transformação
          - 4.1.1 Normalidade
          - 4.1.2 Transformação
        - 4.2 Estacionariedade e diferenciação
          - 4.2.1 Estacionariedade
          - 4.2.2 Diferenciação
        - 4.3 Autocorrelação
          - 4.3.1 Função de autocorrelação (ACF)
          - 4.3.2 Função de autocorrelação parcial (PACF)
  - 5. Modelos de série temporal
        - 5.1 ARIMA (AutoRegression Integrated Moving Average)
          - 5.1.1 Criação e comparação entre modelos ARIMA
  - 6. Previsão série temporal
        - 6.1 ARIMA
- Referências Bibliográficas

## Introdução

<div style="text-align: justify">O setor automobilístico é um importante setor que indica a situação econômica do país. Segundo o site Bonevau, <blockquote>historicamente, a indústria automobilística possui um expressivo peso na economia e no desenvolvimento do país. Seja pela sua capacidade de criar demanda para uma grande cadeia de indústrias paralelas ou para gerar empregos, as montadoras sempre foram um segmento bastante valorizado no Brasil e no mundo.</blockquote> Dada essa importância, iremos analisar os dados da vendas de comerciais leves, também conhecidos como pequenos caminhões de carga, também conhecidos com furgões ou vans, que, segundo a definição do site icaminhões, <blockquote>os comerciais leves são os veículos de carga com peso acima de 3.000 quilos a, no máximo, 7 toneladas. A presença dos furgões nos grandes centros urbanos do Brasil vem tornando-se cada vez maior por conta das crescentes restrições à circulação dos caminhões.</blockquote> Os dados das vendas foram coletados pela Federação Nacional da Distribuição de Veículos Automotores e mantidos/atualizados pelo banco central do Brasil (BCB), cujo link pode ser acessado por <a href="https://dados.gov.br/dataset/7385-vendas-de-veiculos-pelas-concessionarias-comerciais-leves#"> aqui </a>, os dados de venda são referentes ao meses dos anos de 1990 até 2021, no momento que foi feita a requisição dos dados.</div><br/> 

## Análise geral

<div style="text-align: justify">O objetivo da análise desses dados é entender mais a fundo sobre as vendas e tirar alguns insights interessantes sobre e entender como podemos utilizá-los para algo mais interessante. Os dados das vendas são composto pelo mês de cada ano e seus respectivo número de vendas. Depois de entender os dados e o seu objetivo, agora podemos começar a análise.</div><br/>

### 1) Histograma<br/><br/>

<div style="text-align: justify">O histograma é um gráfico de barras que mostra uma distribuição de frequências de determinado evento, ou seja, mostra a quantidade de vezes que ocorreu aquele evento. No nosso exemplo, mostraremos a quantidade absoluta de comerciais leves vendidos em todos os meses durante o período, observe a imagem abaixo:</div><br/>

![Histograma venda mensal](histograma_venda_mensal.png "Histograma venda mensal comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">De acordo com o histograma do conjunto de dados analisados, percebe-se que é ele é um de “cauda à direita”, isto é, grande maioria das quantidades de vendas mensais estão a direita do histograma, especificamente  maior quantidade de vendas entre 15000 a 28000 unidades, aproximadamente.</div><br/>

### 2) Medidas de tendência central<br/><br/>

<div style="text-align: justify">As medidas de tendência central são nada mais que valores que representam todo o conjunto de dados ou amostra. As medidas mais utilizadas são a <b>média</b>, <b>mediana</b> e <b>moda</b>.</div><br/>

#### 2.1) Média<br/><br/>

<div style="text-align: justify">A média, o mais conhecido dentre os outros, é o somatório dos valores do conjunto/amostra dividido pela quantidade total de cada valor. No conjunto de dados analisado , a média mensal de vendas de comerciais leves durante o período é de, aproximadamente, <b>28.988</b> unidades.</div><br/>


#### 2.2) Mediana<br/><br/>

<div style="text-align: justify">A mediana, diferentemente da média, é o valor central do conjunto/amostra de dados, ou seja, o valor que separa o conjunto/amostra de dados ao meio, desde que seja organizados de maneira crescente ou decrescente. No conjunto de dados analisado, a mediana foi de  <b>24.031</b> comerciais vendidos.</div><br/>

#### 2.3) Moda

<div style="text-align: justify">A moda é a quantidade de vezes que um valor repete-se em um conjunto/amostra de dados. Se um conjunto tiver 2 valores repetidos é bimodal, 3 valores é trimodal e assim sucessivamente. Caso não tenha nenhum valor repetido é amodal. No conjunto de dados analisado, a moda foi de <b>17.333</b> comerciais leves vendidos, fato que ocorreu nos meses de <b>maio</b> e <b>julho</b> dos anos de <b>1994</b> e <b>2004</b>, respectivamente.</div><br/>

### 3) Medidas de dispersão<br/><br/>

<div style="text-align: justify">Segundo a definição da professora Rosimar Gouveia, <blockquote>Medidas de dispersão são parâmetros estatísticos usados para determinar o grau de variabilidade dos dados de um conjunto de valores.
A utilização desses parâmetros tornam a análise de uma amostra mais confiável, visto que as variáveis de tendência central (média, mediana, moda) muitas vezes encondem a homogeneidade ou não dos dados</blockquote.> As medidas de dispersão mais utilizadas são <b>variância</b> e <b>desvio padrão</b>.</div><br/>

#### 3.1) Variância<br/><br/>

<div style="text-align: justify"><blockquote>A variância é determinada pela média dos quadrados das diferenças entre cada uma das observações e a média aritmética da amostra,</blockquote> segundo Rosimar Gouveia. No conjunto de dados analisado, a variância foi de <b>271.004.287,7</b> unidades² no período, ou seja, a quantidade das vendas mensais do conjunto são bastante heterogêneas.</div><br/>

#### 3.2) Desvio Padrão<br/><br/>

<div style="text-align: justify"><blockquote>O desvio padrão é definido como a raiz quadrada da variância. Desta forma, a unidade de medida do desvio padrão será a mesma da unidade de medida dos dados, o que não acontece com a variância,</blockquote> segundo Rosimar Gouveia. No conjunto de dados analisado, o desvio padrão de comerciais vendidos durante o período é de <b>16.462</b> unidades, mostrando uma grande dispersão dos dados.</div><br/>

### 4) Medidas de posição<br/><br/>

<div style="text-align: justify">As medidas de posição serve para localização dos dados para o conjunto. Para isso são utilizados os fractis, que é a divisão do conjunto de dados em partes iguais (Quartis, percentis, mediana, …), sendo os quartis os mais utilizado para medida de posição.</div><br/>

#### 4.1) Quartis<br/><br/>

<div style="text-align: justify">Os quartis tem a função de dividir os dados, de ordem crescente ou descrecente, de forma a separar em quarto partes iguais. A forma mais fácil de visualizar os quartis são através dos gráficos de caixa, também conhecido como “boxplot”. Abaixo vamos uma descrição detalhada do conjunto com o boxplot.</div><br/>

![Boxplot venda mensal periodo](boxplot_venda_mensal_periodo.png "Boxplot venda mensal comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

count    384.0
mean     28988.0
std      16462.0
min      5531.0
25%      17830.0
50%      24031.0
75%      35933.0
max      79746.0

<div style="text-align: justify">O gráfico do boxplot funciona da seguinte maneira, olhando da esquerda para direita, a primeira linha vertical é o valor mínimo (min), a primeira linha do retângulo é o primeiro quartil (Q1 – 25%), a segunda linha destacada dentro do retângulo é o segundo quartil (Q2 – 50%), é a mediana dos dados, a segunda linha que fecha o retângulo é o terceiro quartil (Q3 – 75%), a linha vertical final é o valor máximo dos dados, e as bolinhas coloridas em vermelho são os outliers, ou seja, valores discrepantes do conjunto de dados.
O que da para inferir nesse gráfico de caixa é que:<br/> 1) Amplitude dos dados de venda, que é a diferença entre o valor máximo e valor mínimo, é muito grande, ocasionando uma maior variação dos dados, confirmando também através do desvio padrão.<br/> 2) O retângulo contém 50% de vendas de todo o período, juntamente com a sua mediana. Como esta está mais próxima do primeiro quartil, é correto afirmar que os dados estão são positivamente assimétricos, ou seja, as vendas estão com um comportamento de uma distribuição assimétrica positiva. Saber o tipo de distribuição dos dados é muito importante mais a frente na hora de fazer possíveis inferências estatísticas.<br/> 3) Existem muitos outliers presente no boxplot, sendo necessário averiguar o porquê desse tipo de comportamento deles.</div><br/>

### 5) Outliers<br/><br/>

<div style="text-align: justify">Outliers são valores que estão muito acima ou muito abaixo dos valores máximos e mínimos do boxplot. No conjunto de dados analisados, as vendas de alguns meses do ano no período foram muito acima do máximo do gráfico boxplot. Abaixo, está um gráfico de barra com todos os outliers.</div><br/>

![Gráfico barra outliers](grafico_barra_outliers.png "Gráfico barra outliers comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

Olhando o gráfico vemos que grande partes das vendas acima do valor de venda máximo estão entre os anos de 2010, 2011, 2012 e 2013, sendo os meses de dezembro, dezembro, agosto e dezembro as maiores vendas mensais de cada ano, respectivamente. A partir dai já podem surgir uma pergunta  bastante pertinente sobre esses outliers:

- Por que nesses anos houveram as maiores vendas de comerciais leves?

Antes de responder essa pergunta, será apresentado outro gráfico do tipo boxplot para as vendas dos meses que foram identificados como outliers, juntamente com as medidas de posição de cada ano, exceto o ano de 2010 que tem apenas um único mês.

![Boxplot outliers venda anual](boxplot_outliers_anual.png "Boxplot outliers venda anual comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>
     
data | count | mean | std | min | 25% | 50% <br/>| 75% | max<br/>                                                      
2011| 8.0 | 68871.25 | 4629.76 | 64826.0 65165.0 | 67406.0 | 71428.25 | 78089.0<br/>
2012 | 9.0 | 69903.67 | 6586.35 | 63926.0 | 64524.0 | 66073.0 | 77127.00 | 79746.0<br/>
2013 | 10.0 | 71081.30 | 3815.98 | 65155.0  | 68999.0 | 70939.5 | 73527.75 | 77572.0

<div style="text-align: justify">Visualizando o gráfico e os dados de medida de posição anual, percebe-se que houver uma maior dispersão de vendas no ano de 2012, enquanto que no ano de 2013 teve uma menor dispersão de dados (diferença entre os valor máximo e mínimo), mas com uma mediana maior do que os outros anos, confirmando uma maior venda naquele ano. Vale ressaltar que está sendo analisado <b>SOMENTE</b> os outliers dos meses entre o período de 1990 a 2021.</div><br/>

Agora respondendo a pergunta feita anteriormente:

<div style="text-align: justify">1) O denominador comum entre esses anos, principalmente nos anos de 2011-2013 foi a <b>redução da alíquota do imposto de produtos industrializados (IPI)</b> concedidos pelo governo federal, cujo mais informações podem ser acessados por aqui: <a href="https://oglobo.globo.com/politica/venda-de-carros-comerciais-leves-recorde-em-dezembro-2843534">2010</a> <a href="https://www.uol.com.br/carros/noticias/reuters/2012/01/02/venda-de-automoveis-e-comerciais-leves-em-2011-bate-recorde.htm">2011</a> <a href="https://abde.org.br/noticias/venda-de-carros-caminhoes-e-onibus-bate-recorde-em-2012/">2012</a> <a href="https://autoesporte.globo.com/carros/noticia/2014/01/venda-de-carros-e-comerciais-leves-e-recorde-em-dezembro-de-2013.ghtml">2013</a>.</div>


<div style="text-align: justify">Como falamos sobre o desempenho dos meses dos anos detectados como outliers, também é interessante ver o desempenho de vendas anual durante o periodo:</div><br/>

![Boxplot venda anual periodo](boxplot_venda_anual_periodo.png "Boxplot venda anual comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

data count mean std min 25% 50% 75%<br/> max<br/>                                                                        
1990  12.0  10702.67  3346.55   5531.0   8114.25  11233.0  13208.00   15328.0<br/>
1991  12.0  10689.92  2460.11   5978.0   9143.00  10855.5  12243.25   15026.0<br/>
1992  12.0  10328.25  2285.60   6048.0   9458.75  11398.0  11641.50   12596.0<br/>
1993  12.0  14400.50  2067.73  11062.0  13321.50  14083.5  15099.50  18203.0<br/>
1994  12.0  17794.92  3152.20  13216.0  16146.00  17913.5  19203.50  25138.0<br/>
1995  12.0  19688.00  2684.78  16665.0  18555.25  18999.0  19775.25  27148.0<br/>
1996  12.0  22416.17  2695.13  16487.0  20785.75  22803.5  24926.00  25171.0<br/>
<i>1997  12.0  24459.58  3316.36  18779.0  22298.75  25015.0  26642.75  29935.0</i><br/>
1998  12.0  20970.75  3005.79  16483.0  18378.00  20318.0  23567.25  25420.0<br/>
1999  12.0  14310.58  2762.29   9068.0  11611.50  15379.0  15776.00  17698.0<br/>
2000  12.0  17304.17  5133.15   9414.0  14355.50  18224.0  20084.50  26881.0<br/>
2001  12.0  22820.42  2304.91  19380.0  20567.75  22969.5  24301.50  26490.0<br/>
2002  12.0  20052.83  1996.12  16472.0  18709.50  20708.0  21206.25  22981.0<br/>
2003  12.0  17846.42  1663.46  15856.0  16939.00  17249.5  18237.00  21845.0<br/>
2004  12.0  18369.00  3111.63  13665.0  17172.25  18004.0  19962.75  25599.0<br/>
2005  12.0  20940.17  2652.57  16164.0  19851.50  21235.0  22193.50  26308.0<br/>
2006  12.0  22854.42  2888.10  17991.0  21309.75  22970.0  25148.50  27459.0<br/>
<b><i>2007  12.0  30410.33  5987.99  20824.0  27223.25  30022.5  36262.25  38719.0</i></b><br/>
<b><i>2008  12.0  39644.42  5142.76  32279.0  35163.50  39941.0  42994.75  47969.0</i></b><br/>
<b><i>2009  12.0  44161.58  6207.78  31540.0  41336.75  46173.0  46905.75  54459.0</i></b><br/>
<b><i>2010  12.0  56448.08  8680.21  41847.0  52945.25  57830.0  59929.50  73539.0</i></b><br/>
<b><i>2011  12.0  64941.58  7396.32  49807.0  61015.50  65055.0  68756.50  78089.0</i></b><br/>
<b><i>2012  12.0  66041.42  9071.54  50703.0  62069.75  64578.0  72657.00  79746.0</i></b><br/>
<b><i>2013  12.0  68400.25  7347.69  51024.0  65962.75  70564.0  72857.25  77572.0</i></b><br/>
<b><i>2014  12.0  44466.00  3610.28  38739.0  41989.75  44904.0  45935.75  50650.0</i></b><br/>
<b><i>2015  12.0  29517.25  4470.29  23376.0  26972.75  29154.5  32399.00  37720.0</i></b><br/>
<i>2016  12.0  24849.58  3429.00  18424.0  23608.00  25210.0  27184.75  29121.0</i><br/>
<i>2017  12.0  26361.92  3783.38  20017.0  24715.25  26981.5  28518.00  32865.0</i><br/>
<b><i>2018  12.0  30701.17  4109.21  21857.0  28640.25  31322.5  33146.75  35887.0</i></b><br/>
<b><i>2019  12.0  33078.92  3571.01  26861.0  31374.50  34468.0  35637.00  36642.0</i></b><br/>
<i>2020  12.0  27935.50  9218.84  11857.0  23507.00  28842.0  36708.50  38118.0</i><br/>
<b><i>2021  12.0  34710.17  2970.62  30135.0  32487.25  35109.0  36685.25  38821.0</i></b>

<div style="text-align: justify">Observando o gráfico boxplot do desempenho de vendas de carros anual do período, e comparando com somatório de todo o período mensal, percebe-se muitas coisas interessantes. Vamos analisar o gráfico junto com a estatística descritiva do gráfico em questão das vendas anuais. Os anos que estão grifados em <b>negrito</b> são aqueles  que a venda média anual superou a venda  média de todo o período, os grifados em <i>itálico</i> são aqueles onde a venda mediana anual superou a venda mediana, e os grifados em <b><i>negrito e itálico</i></b> são aqueles onde a venda média e mediana anual superou a venda média e mediana de todo o período.<br/>
O que ficou evidente nesse gráfico foram que de 2007 a 2013 houve um crescimento muito acelerado na venda dos comerciais leves, cujo alguns motivos, como a redução da alíquota do IPI, falado anteriormente, favoreceram, e muito, nas vendas, e o ano de 2013 podemos afirmar que foi o ano dourado de vendas dos comerciais leves.</div><br/>

### 6) Teste de normalidade<br/><br/>

<div style="text-align: justify">Saber se os dados estão numa distribuição normal é importante para fazer a estatística inferencial, seja para fazer teste de hipóteses ou até mesmo para a modelagem de dados para a previsão nas séries temporais, que será abordado posteriormente. Existem algumas formas de verificar a distribuição de dados, abaixo veremos algumas formas.</div><br/>

#### 6.1) Histograma com linha de distribuição

<div style="text-align: justify">Esse método já foi visto no item [1](), já que, além de servir para a visualização de distribuição de frequências, também serve para visualização da distribuição dos dados. Abaixo veremos a distribuição dos dados.</div><br/>

![Histograma distribuição venda mensal](histograma_distribuicao_venda_mensal.png "Histograma distribuição venda mensal")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">A diferença desse gráfico para o [histograma](1) é que ele vem com uma linha de distribuição que auxilia para uma melhor definição do tipo da distribuição. E olhando essa linha no gráfico, vemos que a distribuição é assimétrica positiva, ou à direita. Isso significa que a [média](2.1) é maior do que a [moda](2.3).</div><br/>

#### 6.2) Teste de Shapiro-Wilk<br/><br/>

<div style="text-align: justify">É um teste estatístico para aferir a distribuição normal de um conjunto de dados/registros. A sua única limitação é que só consegue fazer esse teste o conjunto com uma quantidade menor ou igual a 5000 dados/registros. Abaixo veremos o teste para as vendas de comerciais leves ao longo do período de 1990 a 2021.</div><br/>

Teste de Shapiro-Wilk
**Critério: Nível de significancia de 0.05 ou 5% (mais utilizado)**
**Se p > 0.05 (distribuição normal)**
Estatística do teste: 0.8769716024398804
**Valor p: 6.209090978297413e-17**

<div style="text-align: justify">O teste corrobora aquilo que foi visto no histograma (6.1), mostrando uma distribuição não-normal, ou seja, uma distribuição assimétrica positiva.</div>

## Série temporal

###  1) Definição<br/><br/>

<div style="text-align: justify">Como foi observado nos itens anteriores, percebemos que ao longo do tempo foi possível ver valores de vendas de meses ao longo de um período, e isso é chamado de série temporal, onde ao longo de um determinado tempo, desde segundo até anos, observamos valores durante o seu intervalo. E é a partir dessas séries temporais que existem a possibilidade de fazer previsões para tempos futuros, e essas previsões podem servir para várias área como varejo, gestão, planejamento, meteorologia, dentre outros, servindo como um referencial para determinado tipo de situação que deseja-se resolver. Abaixo veremos o gráfico da série temporal</div><br/>

![Gráfico série temporal comerciais leves](serie_temporal_comerciais_leves.png "Série temporal venda mensal comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">No gráfico, percebe-se que de 2007 a 2013, houve o melhor desempenho na venda de comerciais leves vendidos, enquanto que no final do ano de 2019 e até meados de 2020 houve o pior desempenho de venda.</div><br/>

### 2) Média móvel<br/><br/>

<div style="text-align: justify">A média móvel é uma média que se move conforme o tempo de referência. Ela é utilizada para suavização de séries temporais, isto refere-se, principalmente, a séries que possuem um ato grau de oscilação dos picos durante o período, por exemplo a média móvel semanal do COVID-19, e determinação de tendência, esta que pode ser ascendente (subida), descendente (descida) e sem tendência. Sobre a tendência, falaremos mais dela quando trataremos de decomposição de série temporal. Porém, vale ressaltar que ela <b>não</b> serve para fazer previsão da série. Abaixo veremos a média móvel dos valores mensais da série temporal.</div><br/>

![Gráfico média móvel comerciais leves](media_movel_comerciais_leves.png "Gráfico média móvel vs série temporal comerciais leves")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/> 

<div style="text-align: justify">Visualizando a média móvel (linha vermelha), não é possível perceber o tipo de tendência que essa série apresenta para os próximos meses.</div><br/>

### 3) Decomposição série temporal<br/><br/> 

<div style="text-align: justify">A série	temporal ela pode ser decomposta em algumas partes, para um entendimento aprofundado da mesma. E estas partes são:<br/><br/>

<b>Tendência</b> → São mudanças graduais em longo prazo, podendo ser uma tendência crescente (ascendente), decrescente (descendente) ou não haver tendência.<br/>

<b>Sazonalidade</b> → São oscilações ascendentes e descendentes que ocorrem em um determinado período. Um exemplo disso são o número de voos durante a época de verão, onde nesse período é comum o aumento por causa das férias, festividades de final de ano, etc.<br/>

<b>Resíduo</b> → Apresenta movimentos ascendentes e descendentes da série após a retirada do efeito de tendência ou sazonal (sequência de variáveis aleatórias). Os resíduos tem suma importância na hora da montagem dos modelos de série temporais, já que indicam se os modelos estão bem ajustados ou não.<br/>
Existem 2 tipos de modelos de decomposição da série temporal:</div>

- Aditivo → Série temporal (Zt) é o resultado da soma da tendência (Tt), sazonalidade (St) e resíduo (Rt)

  Zt = Tt + St + Rt

- Multiplicativo → Série temporal (Zt) é o resultado da soma da tendência (Tt), sazonalidade (St) e resíduo (Rt)

  Zt = Tt x St x Rt

<div style="text-align: justify">A diferença entre eles é que na decomposição multiplicativa normalmente fornece os melhores resultados quando existe uma relação entre a sazonalidade e os dados, isto é, quando aumenta a sazonalidade com o aumento dos valores dos dados ou quando diminui a sazonalidade com a diminuição dos valores dos dados. Caso não haja a relação entre a sazonalidade e dos dados, o método aditivo é o mais recomendado. Como visto no gráfico da série temporal, os valores aumentam ou diminui e não depende exclusivamente da sazonalidade, então foi optado por um modelo aditivo. Abaixo veremos o gráfico da decomposição da série temporal com o modelo aditivo.</div><br/>

![Gráfico decomposição série temporal](decomposicao_serie_temporal.png "Decomposição da série temporal")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">E aqui está a decomposição da série, de cima para baixo, com o gráficos da série original, tendência, sazonalidade e resíduo, respectivamente. Como podem ver no gráfico, a tendência não está muito bem definida, mas a sazonalidade está muito bem definida, algo bem relevantes para a modelagem dos dados para o modelo da série temporal. Outro ponto para destacar é que foi feita a decomposição da série temporal dos meses de 1990 até 2020, isso acontece porque deixaremos os dados do ano de 2021 para futura métrica de avaliação do modelo, que será vista mais adiante.</div><br/>

### 4) Modelagem de dados <br/><br/>

<div style="text-align: justify">Existem vários modelos para fazer previsão, mas para aplicar esses modelos, é necessário antes fazer uma modelagem dos dados. A modelagem é necessária para deixar os dados prontos para o modelo que for empregado e que tenha uma melhor performance na hora da previsão dos dados.</div><br/>

#### 4.1) Normalidade e Transformação<br/><br/>

#### 4.1.1) Normalidade<br/><br/>

<div style="text-align: justify">Normalidade tem o objetivo de transformar a distribuição da série temporal em uma distribuição aproximadamente normal (gaussiana), cujo objetivo é fazer com que os modelos fiquem mais eficientes na hora de fazer a previsão dos valores.<br/>
Esse teste de [normalidade](6) já foi visto anteriormente, com o teste de [Shapiro-Wilk](6.2), juntamente com o histograma da série temporal. A diferença agora é a presença de mais uma nova ferramenta para a visualização da normalidade: gráfico QQ-plot.</div><br/>

![Gráfico normalidade QQplot](qqplot_serie_temporal.png "Gráfico normalidade QQplot")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">No gráfico QQplot, para uma distribuição ser normal ou aproximadamente normal, os dados, em sua maioria, tem que estar acima da linha vermelha. Nos dados da série temporal mostram claramente que os dados **não** estão normalmente distribuídos.
Percebe-se que tanto o gráfico QQplot com o teste de Shapiro-Wilk mostram que os dados não estão normalizados, sendo necessário uma transformação.</div><br/>

#### 4.1.2) Transformação<br/><br/>

<div style="text-align: justify">A transformação dos dados é necessária com a função de transformar os dados da série temporal em dados próximos da distribuição normal.
Caso a série temporal não esteja normalizada, que é o caso da nossa série temporal, existem vários tipos de transformação para os dados da série temporal.</div><br/>

- Transformação **log**<br/>
  <div style="text-align: justify">A transformação mais utilizada, indicada para distribuição assimétrica positiva e variação crescente com a média, só podendo ser utilizado caso os dados da série temporal sejam somente positivos. Sua função é tirar o logaritmo de cada dado da série temporal, pode-se usar qualquer tipo de logaritmo, sendo os mais utilizados o logaritmo natural e o logaritmo na base 10.</div><br/>

- Transformação **exponencial** <br/>
  <div style="text-align: justify">Caso a série temporal possuam dados zerados e/ou negativos, usa-se a transformação exponencial, que resume-se a tirar a raiz cúbica ou quadrada dos dados.</div><br/>

- Transformação **Box-Cox**<br/>
  <div style="text-align: justify">Também existe a transformação Box-Cox, onde a série temporal só pode possuir valores positivos, igual a transformação utilizando log.</div>

<div style="text-align: justify">Como a transformação <b>log</b> é a opção mais utilizada, não seria diferente aqui, e ele também foi escolhido para os dados da série temporal, optando pelo logaritmo na base 10 por questão pessoal, somente. Agora faremos o teste de normalidade nos dados transformados com QQplot e teste estatístico de Shapiro-Wilk.</div><br/>

 ![Gráfico normalidade QQplot transformada](qqplot_transformada_serie_temporal.png "Gráfico normalidade QQplot série transformada")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">Observando o gráfico QQplot após a transformação, é nítida a diferença da normalidade. Agora é necessário ver o teste estatístico de Shapiro-Wilk para confirmar, ou não, a normalidade dos dados.</div><br/>

Teste de Shapiro-Wilk
**Critério: Nível de significância de 0.05 ou 5% (mais utilizado)**
Se p > 0.05 (distribuição normal)
**Estatística do teste: 0.9842071533203125**
**Valor p: 0.0004322609747759998**

<div style="text-align: justify">Apesar do gráfico QQplot mostra que, após a transformação, os dados, aparentemente, estão normais. Entretanto, o teste de Shapiro-Wilk não confirma a normalidade dos dados após a transformação. O que pode ter acontecido é que alguns dados de venda estejam acima da normalidade (outliers), fazendo com que a transformação não tenha atingindo a normalidade. Creio que se os outliers fossem removidos, a distribuição ficaria normal, entretanto perderiamos dados importantes na hora de fazer análises estatísticas e modelagem dos dados para criação de modelos de previsão mais robustos, sem contar que foram utilizados outros métodos de transformação, e nenhum conseguiu fazer com que a distribuição ficasse normal. Então, nesse caso, considerando todas as variáveis desses dados, vamos considerar que os dados estão normais.
Após atestada a normalidade dos dados da série temporal, agora é necessário verificar a estacionariedade da mesma.</div><br/>

#### 4.2) Estacionariedade e diferenciação<br/><br/>

#### 4.2.1) Estacionariedade<br/><br/>

<div style="text-align: justify">Após a normalização dos dados, é necessário verificar se a série temporal está estacionária. Série temporal estacionária é aquela que se desenvolvem aleatoriamente no tempo através de uma <b>média constante</b>, e esse é mais um requisito importante para fazer um modelo adequado para previsão.
Séries não estacionárias mudam de comportamento por inclinação ou mudança de nível.<br/> Por exemplo, séries temporais com sazonalidade não são estacionárias, porque a média não é constante ao longo do tempo.
Quando ocorrem mudanças repentinas na série temporal tem-se séries temporais não estacionárias <b>explosivas</b>(Por exemplo, crescimento de bactérias).<br/>
Existem vários testes estatísticos para determinar a estacionariedade da série temporal, como KPSS, Dickey-Fuller, Phillips-Perron, dentre outros.
E para confirmar a estacionariedade, optou-se por utilizar o teste estatístico como o KPSS, por exemplo. Abaixo veremos os resultados do teste para a série temporal após transformação:</div><br/>

Teste de estacionariedade KPSS
H0 - Não estacionária: estatística do teste > valor crítico
HA - Estacionária: estatística do teste < valor crítico
**Estatística do teste: 1.3152953918238164**
Valor p: 0.01
Número de lags: 17
Valores críticos:
10% : 0.3470
**5% : 0.4630**
2.5% : 0.5740
1% : 0.7390

Como podemos observar, a série temporal está "normalizada", mas não está estacionária. Fazendo com que seja necessário fazer uma diferenciação nos dados.

#### 4.2.2) Diferenciação<br/><br/>

<div style="text-align: justify">A diferenciação tem o objetivo de transformar a série não estacionária em estacionária. E é um processo que faz a diferença de dois períodos consecutivos.<br/>
Pode-se fazer quantas diferenciações forem necessárias para obter a estacionariedade, a ressalva está em ter cuidado para que a diferenciação não afete a interdependência da série. Normalmente são feitas até 2 diferenciações para as series temporais para deixar a série temporal estacionária, chamando-as de primeira e segunda ordem, respectivamente.<br/>
A diferenciação remove os sinais de tendência e sazonalidade e reduz a variância.
Abaixo veremos o resultado da série temporal após a diferenciação dos dados:</div><br/>

Teste de estacionariedade KPSS
H0 - Não estacionária: estatística do teste > valor crítico
HA - Estacionária: estatística do teste < valor crítico
**Estatística do teste: 0.054780214818354**
Valor p: 0.1
Número de lags: 17
Valores críticos:
10% : 0.3470
**5% : 0.4630**
2.5% : 0.5740
1% : 0.7390

<div style="text-align: justify">Como era de se esperar, os dados da série temporal não são estacionários, já que, por pouco, também não ficaram normalizados após a transformação. Entretanto, consideraremos como sendo normalmente distribuída por causa do gráfico QQ-plot.</div><br/>

#### 4.3) Autocorrelação<br/><br/>

<div style="text-align: justify">É a correlação de determinados <b>períodos anteriores</b> com o <b>período atual</b>. Todo período com esse período de correlação é denominado <b>lag</b>.<br/>
A análise de autocorrelação é um pressuposto para se criar modelos de previsões, sendo que as correlações podem ser positivas, negativas ou nem existir correlação.
Exemplo: As vendas de temporada das férias de verão deste ano está muito parecida com as vendas das temporadas dos últimos 5 anos.<br/>
Alguns testes para avaliação da autocorrelação são o <b>ACF</b> e <b>PACF</b>, função de autocorrelação e função de autocorrelação parcial, respectivamente.</div><br/>


#### 4.3.1) Função de autocorrelação (ACF)<br/><br/>
<div style="text-align: justify">A função de autocorrelação (ACF) analisa os dados (lags) vizinhos, na sequência, seja anterior ou superior ao dado atual.
Abaixo veremos o gráfico ACF da série temporal com 60 lags:</div><br/>

![Gráfico ACF](autocorrelacao.png "Gráfico de autocorrelação com 60 lags")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">Como podemos ver, grande parte dos lags estão dentro do intervalo de confiança (azul), algo muito positivo para a modelagem dos dados.</div><br/>

#### 4.3.2) Função de autocorrelação parcial (PACF)
A função de autocorrelação parcial (PACF) analisa os dados (lags) de forma (aleatória).
Abaixo veremos o gráfico PACF da série temporal com 60 lags:

 ![Gráfico PACF](autocorrelacao_parcial.png "Gráfico de autocorrelação parcial com 60 lags")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">Como no gráfico de correlação, a grande maioria dos lags estão dentro do intervalo de confiança. O que também significa um ótimo sinal para o modelo.</div><br/>

<div style="text-align: justify">Tanto o ACF quanto o PACF são ótimo indicadores para a modelagem da série temporal. E diz que o melhor modelo é aquele onde os lag, tirando o principal, o primeiro do gráfico, tem que estarem dentro do intervalo de confiança da série. Mas caso o teste ACF e/ou PACF indiquem um alto grau de correlação entre os lags, não significa que não seja possível fazer a modelagem da série temporal. Até porque, esse teste terá maior relevância na hora que o modelo ARIMA estiver pronto, e ai sim servirá de um ótimo norteador do quão bom o modelo está, através das análises dos resíduos do modelo criado. Aqui, esses testes servem de indicativo dos dados para o modelo, uma espécie de norte.</div><br/>

### 5) Modelos série temporal<br/><br/>

<div style="text-align: justify">Após a modelagem, os dados estão prontos para serem aplicado nos modelos. Abaixo listaremos alguns modelos para esses dados.</div><br/>

#### 5.1) ARIMA (AutoRegression Integrated Moving Average)<br/><br/>

<div style="text-align: justify">O modelo ARIMA é um modelo composto por outros 3  componentes de modelos: Autoregressivo (AR) integrado (I) de média móvel (MA), sendo o componente MA não refere-se a média móvel da série temporal. Segue abaixo uma explicação mais detalhada de cada componente do modelo:</div><br/>

- Autoregressivo (AR):<br/>
  <div style="text-align: justify">Indica que a variável é regressada em seus valores anteriores.</div>
- Integrado (I):<br/>
  <div style="text-align: justify">Indica que os valores de dados foram substituídos com a diferença entre seus valores e o seus valores anteriores, também conhecido como diferenciação dos dados.</div>
- Média móvel (MA):<br/>
  <div style="text-align: justify">Indica que o erro de regressão é uma combinação linear dos termos de erro dos valores passados. Diferentemente da média móvel da série temporal, que cria uma série com a média dos dados em relação ao tempo de referência.</div>

#### 5.1.1) Criação e comparação entre modelos ARIMA<br/><br/>

<div style="text-align: justify">Após breve explicação sobre o modelo ARIMA e seus componentes , agora é só combinar os parâmetros e ver os resultado do modelo que é gerado. Há um tempo atrás, tinha que testar cada componente e verificar o resultado do modelo, para depois testar todos os componentes. Normalmente os valores eram de 0 até 10, ou seja, era um trabalho enorme para descobrir o modelo ARIMA ideal para aquela série temporal, sendo utilizado até a função de autocorrelação (ACF) e a função de autocorrelação parcial (PACF) para determinar a ordem dos parâmetros do modelo. Hoje, é utilizado um buscador automático de ARIMA, chamado auto ARIMA, onde este vai testando automaticamente cada ordem de parâmetro do modelo. O único ponto negativo do auto ARIMA é seu alto custo computacional, já que vai testar todos os valores que foi colocado para definir o melhor modelo, levando em consideração a quantidade de dados presente na série temporal.<br/>
Para saber qual é o melhor modelo, existem algumas métricas que ajudam a comparar os modelos ARIMA com os mais variados componentes para ver qual se adequou melhor aos dados da série temporal, como o critério de informação Akaide (AIC), o critério de informação Akaide corrigido (AICc) e o critério de informação bayesiano (BIC). Sem mostrar e entrar em detalhes nas fórmulas de cada critério, o AIC e BIC são os mais utilizados para avaliar modelos ARIMA, sendo o AIC o mais utilizado. Em relação ao entendimento da métrica, quanto menor a pontuação do AIC ou BIC para aquele modelo, melhor ele é. Adiante veremos abaixo qual melhor modelo que o auto ARIMA escolheu para os dados da nossa série temporal:</div><br/>

<div style="text-align: justify">Para a série temporal que estamos usando, o melhor modelo ARIMA para ele foi o (1, 0, 2)(1, 0, 1), com o AIC = -933.098, portanto será ele que será utilizado, tanto que após a geração desses modelos, automaticamente o auto ARIMA escolhe justamente aquele com o menor AIC, sejam eles positivos ou negativos, o que importa mesmo é selecionar o menor valor.<br/>
Aqui vale explicar um detalhe na geração dos modelos pelo auto ARIMA. O auto ARIMA utiliza o modelo SARIMA, onde o S significa sazonalidade (seasonal), e ele possui os parâmetros (P, D, Q), representados pelo segundo parênteses.<br/> 
Após escolhido o melhor modelo para a série, fazer uma avaliação do modelo. Então é necessário verificar os resíduos do modelo ARIMA criado e avaliar a sua diferenciação, distribuição normal e suas autocorrelações, tanto o ACF quanto o PACF.
Primeiro, veremos o gráfico dos resíduos com o gráfico dele logo abaixo.</div><br/>

![Resíduos ARIMA](residuos_modelo_arima.png "Gráfico resíduos do modelo ARIMA")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">Percebe-se que os resíduos tem uma média e variância constante, o que significa que o modelo ARIMA encaixou bem com os dados e os resíduos são estacionários.
Agora, veremos o gráfico da normalidade do resíduo do modelo ARIMA abaixo.</div><br/>

![Gráfico disribuição residuos ARIMA](distribuicao_normal_residuos.png "Gráfico da distribuição normal dos resíduos do modelo ARIMA")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">No gráfico, percebe-se que os resíduos estão perto de ser normalmente distribuidos, com alguns pontos fora da reta. Para confirmar, basta ver o teste de Shapiro-Wilk para ter mais uma ferramenta para verificação estatística da distribuição dos dados.</div><br/>

Teste de Shapiro-Wilk
Critério: Nível de significancia de 0.05 ou 5% (mais utilizado)
Se p > 0.05 (distribuição normal)
Estatística do teste: 0.9461087584495544
Valor p: 2.1602641897544572e-10

<div style="text-align: justify">Apesar do teste avaliar que os dados do resíduo do modelo ARIMA não estão distribuidos, iremos considerar o que o gráfico mostrou anteriormente.
Agora iremos ver o ACF e PACF dos resíduos do modelo ARIMA:</div><br/>

![Gráfico ACF residuos](autocorrelacao_residuos.png "Gráfico de autocorrelação dos residuos com 60 lags")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

![Gráfico PACF](autocorrelacao_parcial.png "Gráfico de autocorrelação parcial dos residuos com 60 lags")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

<div style="text-align: justify">Tanto o ACF quanto PACF mostram que a grande maioria dos lags estão dentro do intervalo de confiança, mostrando que não correlação entre eles. E mostra que o modelo ARIMA está bom para esse tipo de dados.</div><br/>

### 6) Previsão série temporal<br/><br/>

<div style="text-align: justify">Após toda preparação dos dados, modelagem e testes estatísticos, vem a parte que mais interessa, que é a tentativa de prever algo no futuro. Nesse caso é fazer a previsão de futuras vendas de comerciais leves para os meses do ano de 2022.</div><br/>

#### 6.1) ARIMA<br/><br/>

![Gráfico série + previsão 2022](serie_temporal_previsao.png "Gráfico da série temporal mais previsão para 2022")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

![Gráfico previsão 2022](previsao_vendas_2022.png "Gráfico com a previsão de venda de comerciais leves para o ano de 2022.")
<div align="center">(Fonte: Arquivo pessoal, 2022)</div><br/>

## Referências Bibliográficas

<div style="text-align: justify">BONEVAU, 26 nov 2021. Disponível em: https://www.bovenau.com.br/blog/a-importancia-da-industria-automobilistica/. Acesso em: 19 jan 2022 15:36.</div><br/>

<div style="text-align: justify">ICAMINHÕES, 28 jun 2013. Disponível em: https://caminhoes.icarros.com.br/noticias/caminhoes/top-10:-comerciais-leves-mais-baratos-do-pais/14546.html. Acesso em: 19 jan 2022 15:52.</div><br/>

<div style="text-align: justify">GOUVEIA, Rosimar. TODAMATÉRIA. Disponível em:https://www.todamateria.com.br/medidas-de-dispersao/. Acesso em: 19 jan 2022 23:59</div>