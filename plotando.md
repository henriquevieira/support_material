import pandas as pd
% matplotlib inline # adicionar sempre ao gerar notebooks

df = read_csv('arquivo.csv')

# histograma
df.hist()
ou determinando o tamanho
df.hist(figsize=8,8); # adicione o ponto-e-virgula para não apresentar o codigo gerado
df['coluna'].hist();
outra maneira, é especificando o tipo de plot
df['coluna'].plot(kind='hist');

# barras
Fazendo a contagem para colunas de fatores
df['coluna_fator'].value_counts()
df.set_xlabel("rotulo de X")
df.set_ylabel("rotulo de Y")

fazendo o plot
df['coluna_fator'].value_counts().plot(kind='bar');

# pizza
df['coluna_fator'].value_counts().plot(kind='pie', figsize=(8,8))

# scatter plot
pd.plotting.scatter_matrix(df, figsize=(8,8));

outra maneira

df.plot(x='colunaX', y = 'colunaY', kind='scatter');

# boxplot
df['coluna'].plot(kind='box');


# Criando um gráfico de barras usando matplotlib

import matplotlib.pyplot as plt
% matplotlib inline

plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label');

# Pacotes a carregar

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')

# histograma duplo

plt.hist(df['colunaA'], color='r', alpha=0.5, label='label1')
plt.hist(df['colunaB'], color='b', alpha=0.5, label='label2')
plt.legend()
plt.show()













