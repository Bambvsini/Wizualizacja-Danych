import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import seaborn as sb
from PIL import Image

#zadanie 1
# def f(x):
# 	return 1/x
#
# x=np.arange(1,21)
# wykres = plt.plot(x, f(x), 'g>', label='f(x) = 1/x', linestyle='dotted')
# plt.tick_params(axis='y', labelrotation= 0, labelsize= 7)
# plt.xlabel=('x')
# plt.ylabel=('f(x)')
# plt.ylim(ymin=0 ,ymax=1)
# plt.xlim(xmin=0, xmax=20)
# plt.legend(loc='upper right')
# plt.show()

#zadanie 3
# x=np.arange(0, 30, 0.1)
# plt.plot(x, np.sin(x), label ='sin(x)')
# plt.plot(x, np.cos(x), label ='cos(x)')
# plt.xlabel('x')
# plt.ylabel('wartość funkcji')
# plt.title('Wykres funkcji sin(x) i cos(x)')
# plt.legend(loc='upper right')
# plt.show()

#zadanie 4
# df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
# x = df[0]
# y = df[1]
# d = np.abs(x-y)
# c = np.random.randint(0, 150 , 150)
# plt.scatter(x, y, c=c, s=d)
# plt.show()

#zadanie 5
df = pd.read_excel('imiona.xlsx', header=0)
fig, axs = plt.subplots(3, 1)
grupa = df.groupby('Rok').agg({'Liczba':['sum']})
print(grupa)
lata = df['Rok'].unique()
axs[0].bar(lata, grupa['Liczba']['sum'])
axs[0].xticks(lata)
fig.show()
