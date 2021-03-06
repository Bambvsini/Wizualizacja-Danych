import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df.to_string())
print(df)
print()

#zadanie 2
print(df[(df['Liczba'] > 1000 ) & (df['Rok'] == 2002)])
print(df[df['Imie']=='MATEUSZ'])
print(df.agg({'Liczba': ['sum']}))
print(df.where((df.Rok >= 2000) & (df.Rok <= 2005)).groupby(by='Rok').agg({'Liczba': ['sum']}))
print(df.groupby(by='Plec').agg({'Liczba': ['sum']}))
print(df.sort_values('Liczba', ascending=False).groupby(['Rok','Plec']).nth(0))

#zadanie 3
df=pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
print(df)
print(np.unique(df.Sprzedawca))
print(df.sort_values(by='Utarg').tail())
print(df.groupby(by='Sprzedawca').agg({'idZamowienia':[('count')]}))
print(df.groupby(by='Kraj').agg({'Utarg':['sum']}))
df['year']=pd.DatetimeIndex(df['Data zamowienia']).year
print(df.where(df.Kraj=="Polska").where(df['year']==2005).agg({'Utarg':['sum']}))
print(df.where(df['year']==2004).agg({'Utarg':['mean']}))
