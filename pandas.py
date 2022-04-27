import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5.5, np.nan, 'a'])
s1 = pd.Series([10, 12, 8, 14], index =['a', 'b', 'c', 'd'])


dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [1231313, 32131, 32131313]}
df = pd.DataFrame(dane)

data = pd.date_range('20220420', periods=5)
df = pd.DataFrame(np.random.randn(5, 4), index=data, columns=list('ABCD'))
print(df)

iris_df = pd.read_csv('iris.csv', header=0, sep=',',decimal='.')
print(iris_df)

iris_df.to_csv ('nowy.csv', index=False)

xlsx = pd.ExcelFile('wyniki.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

df.to_excel('nowy.xlsx', sheet_name='Arkusz_1', index=False)

print(s1['a'])
print(s1.a)
print(df['Populacja'])
print(df.Populacja)
print(df.iloc[0],[1])
print(df.loc[0],['Kraj'])
print(df.at[0, 'Kraj'])
print(df.sample(10, replace=True))
print('')

print(iris_df.head(10))
print(iris_df.tail(10))

print(s1[s1 > 10])

print(s1[~(s1 > 10)])
print(s1[(s1 < 13) & (s1 > 8)])

print(df[df['Populacja'] > 10000000])
print(df[(df.Populacja > 10000000) & (df.index.isin([0,2]))])
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))

s1['e'] = '15'
print(s1)

df.loc[3] = ['nowa wartość', 'nowa stolica', 1000000 ]
df.loc[4] = 'nowa wartość'
print(df)

df.drop(4, inplace=True)
print(df)

# df.drop('Kraj', axis=1, inplace=True)
# print(df)

df['Kontynent'] = ["Europa", "Azja", "Ameyka Południowa", "Europa"]
print(df)
print(df.sort_values(by='Kraj'))
grupa = df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))

print(df.groupby(by='Kontynent').agg({'Populacja': ['sum']}))

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()

ts.plot()
plt.show()

dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Populacja': [123113, 32414131, 3131443, 12399913],
        'Kontynent': ["Europa", "Azja", "Ameyka Południowa", "Europa"]}

df = pd.DataFrame(dane)

grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
print(grupa)
grupa.plot(kind='bar', xlabel='Kontynent', ylabel='ludność', rot=0, title="Populacja dla kontynentów")
wykres = grupa.plot.bar()
wykres.set_xlabel('Kontynent')
wykres.set_ylabel('Populacja w mld')
wykres.tick_params(axis='x', labelrotation = 0)
wykres.legend(loc='upper right')
wykres.set_title('Populacja na kontynentach w mld')
plt.savefig('wykres.png')
plt.show()

df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)

grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})

grupa.plot(kind='pie', subplots='true', autopct='%.2f %%', fontsize=20, figsize=(8, 8), colors=['purple', 'blue'])
plt.legend(loc='upper left')
plt.show()

df = pd.DataFrame(ts)
print(df)

df['Średnia krocząca'] = df.rolling(window=120).mean()
df.plot()
plt.legend(['Wartości', 'Średnia z n-elementów'])
plt.show()
