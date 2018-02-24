# Limpando os dados

# verificando os tipos das variaveis
df.dtypes

# listando os nomes de colunas
df.columns.tolist()

## Preenchendo dados faltantes com a média
mean = df['coluna'].mean()

### Substituindo coluna com os valores preenchidos
df['coluna'] = df['coluna'].fillna(mean) 
ou df['coluna'].fillna(mean, inplace=True)

## Removendo duplicatas

### Listar as duplicatas
df.duplicated()

### Contabilizar numero de duplicatas
sum(df.duplicated())

### Remover as duplicatas
df.drop_duplicates(inplace=True)

## Corrigir o tipo da coluna
### De string para datetime
df['coluna'] = pd.to_datetime(df['coluna'])

### De string para inteiro
df['coluna'] = pd.to_numeric(df['coluna'], downcast='signed')

# Atribua novos rótulos às colunas do dataframe
df.columns = new_labels

# Renomeando uma ou mais colunas
df.rename(index=str, columns={'colunaA':'coluna_a', ...}, inplace=True)

# Removendo espaços e deixando como minusculo
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# Remover colunas
df.drop(['colunaA', 'colunaC', 'colunaE'], axis=1, inplace=True)

# contando valores vazios ou NA
df.isnull().sum()

# removendo NAs
df.dropna(inplace=True)

# removendo colunas totalmente NA
df.dropna(axis=1, how='all')

# removendo todas as colunas com NA
df.dropna(axis=1, how='any')

# removendo linha totalmente NA
df.dropna(axis=0, how='all')

# removendo linhas com NA
df.dropna(thresh=0)

# verificar a contagem de valores para uma coluna categorica
df['coluna'].value_counts()

# removendo strings e mantendo somente os valores numericos
exemplo 

df
A   B
1   a2
2   b4
3   c3
4   d1

df['B'].str.extract('(\d+)').astype(int)

A   B
1   2
2   4
3   3
4   1

# retornar quais colunas possuem uma string
df['coluna'].str.contains('/')

# usando apply
# aplicando split em cada valor da coluna
df[coluna].apply(lambda x: x.split("/")[0])

# filter
df.filter(items=['one', 'three'])

# juntar tabelas uma abaixo da outra (row bind)
df_data = [df_1, df_2, df_3]
df = pd.concat(df_data)

# criando colunas
## crie vetor de identificação para o dataframe
id_A = np.repeat('A', df.shape[0])
df['id_A'] = id_A




