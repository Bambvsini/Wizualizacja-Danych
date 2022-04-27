import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#zadanie 1
df = pd.read_excel('imiona.xlsx', header=0)
print(df)
labels = df['Rok'].unique()
grupa = df.groupby(by='Rok').agg({'Liczba': ['sum']})
wykres = grupa.plot(kind='line', figsize=[8, 8])
wykres.set_ylabel('Liczba urodzeń')
wykres.set_xticks(labels)
wykres.tick_params(axis='x', which='major', labelsize='6')

plt.show()
#zadanie 2
grupa2 = df.groupby(by='Plec').agg({'Liczba': ['sum']})
wykres = grupa2.plot(kind='bar', figsize=[8, 8])
wykres.set_ylabel('Liczba dzieci danej płci')

plt.show()

#zadanie 3
grupa3 = df[df['Rok'] > 2012].groupby('Rok').agg({'Liczba':['sum']})
wykres = grupa3.plot(kind='pie', subplots=True, autopct='%.2f %%')
plt.show()

#zadanie 4
df1 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
grupa4 = df1.groupby('Sprzedawca').agg({"idZamowienia": ['count']})
wykres = grupa4.plot(kind='bar',xlabel='Sprzedawca', ylabel='Sprzedaże')
wykres.tick_params(axis='x', labelrotation = 0, labelsize='7')
wykres.set_xlabel('Nazwisko sprzedawcy')
wykres.set_ylabel('Ilośc obsłużonych zamówień')
plt.show()
