import pandas as pd

# Reading '.xlsx' file
PATH = './Database.xlsx'
df   = pd.read_excel(PATH)

# Data Cleaning
df = df.drop(columns=['Receita Média por Compra', 'Plataforma Utilizada', 'Gênero'])
df = df.dropna() # drop all those rows which have any 'nan' value in it.

# Data Treatment
df['Data']          = df['Data'].astype(int)
df                  = df.astype({'Data': 'object', 'Número de Compradores': 'int64', 
                                 'Novos Usuários': 'int64', 'Visualizações na Página': 'int64',
                                 'Usuários Ativos': 'int64'})
df['Receita Total'] = df['Receita Total'].apply(lambda x: "{:.0f} R$".format(x))

print(df)
# df.to_excel('Newfile.xlsx')
# print(df.dtypes)