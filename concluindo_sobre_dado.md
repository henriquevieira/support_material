# Concluindo sobre o dado

# Separando o dado pelo tipo, por exemplo azul e vermelho
df_azul = df[df['coluna_cor'] == 'azul']
df_vermelho = df[df['coluna_cor'] == 'vermelho']

# Groupby

df.groupby('coluna').mean()
df.groupby(['coluna1', 'coluna2'], as_index=False)['coluna3'].mean()

# Query
df.query("coluna_cor == 'azul'")

# Merge
pd.merge(df_A, df_B, left_on=['colunaX'], right_on=['colunaY'])

