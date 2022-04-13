import numpy as np
#
# # zadanie 1
# a=np.arange(4,84,4)
# print(a)
#
# # zadanie 2
# b=np.arange(1.0,10.0,1.0)
# print(b)
# c=b.astype('int32')
# print(c)
#
# # zadanie 3
# def funkcja(n):
#     e=[]
#     for i in range(1,n*n+1):
#         e.append(2**i)
#     d=np.array([e])
#     d=d.reshape((n,n))
#     return d
#
# print(funkcja(3))
#
# # zadanie 4

def funkcja(n,m):
    return np.logspace(1,m,m,base=n,dtype=float)

print(funkcja(2,4))

# # zadanie 5
# def mac_diag(n):
#     return np.diag([a for a in range(n,0,-1)], +2)
#
# print(mac_diag(5))

# zadanie 6

slowo1="marek"
slowo2="marek"
slowo3="mirek"
a=len(slowo1)
b=len(slowo2)
c=len(slowo3)


pusta=np.empty((a,b),dtype='str')
for i in range(0,a):
    pusta[0,i]=slowo1[i]
    pusta[i,0]=slowo2[i]
    pusta[i,i]=slowo3[i]

print(pusta)


# zadanie 7

def generuj(n):
    zera=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if(j>i):
                zera[i,j]=abs(2*(j-i+1))
            else:
                zera[i,j]=abs(2*(i-j+1))

    return zera

print(generuj(3))


# zadanie 8
def podzial(tablica,kierunek):
    if(kierunek=="poziomo" or kierunek=="pionowo"):
        if(tablica.shape[0]%2==1 and kierunek=="poziomo"):
            return "nie możesz tego zrobić, bo wysokość tablicy jest liczbą nieparzystą"
        if(tablica.shape[1]%2==1 and kierunek=="pionowo"):
             return "nie możesz tego zrobić, bo szerokość tablicy jest liczbą nieparzystą"
        else:
            if(kierunek=="poziomo" and tablica.shape[0]%2==0):
                tab1=np.zeros((tablica.shape[0]//2,tablica.shape[1]))
                tab2 = np.zeros((tablica.shape[0]//2, tablica.shape[1]))
                for i in range(0,tab1.shape[0]):
                    for j in range(0,tab1.shape[1]):
                        tab1[i,j]=tablica[i,j]
                for i in range(tab2.shape[0],tablica.shape[0]):
                    for j in range(tab2.shape[0], tablica.shape[0]):
                        tab2[i-tab2.shape[0], j-tab2.shape[0]] = tablica[i, j]
                return tab1,tab2
            if (kierunek == "pionowo" and tablica.shape[1] % 2 == 0):
                tab1 = np.zeros((tablica.shape[0], tablica.shape[1]//2))
                tab2 = np.zeros((tablica.shape[0], tablica.shape[1]//2))
                for i in range(0, tab1.shape[0]):
                    for j in range(0, tab1.shape[1]):
                        tab1[i, j] = tablica[i, j]
                for i in range(tab2.shape[0], tablica.shape[0]):
                    for j in range(tab2.shape[0], tablica.shape[0]):
                        tab2[i - tab2.shape[0], j - tab2.shape[0]] = tablica[i, j]
                return tab1, tab2


    else:
        return "nastepnym razem wpisz jako kierunek 'pionowo' lub 'poziomo'"


# zadanie 9
r=input("podaj róznicę(int)")
a1=input("podaj 1 wyraz ciągu(int)")
r=int(r)
a1=int(a1)

list=[a1+r*i for i in range(0,25)]


macierz=np.zeros((5,5))
licznik=0
for i in range(0,5):
    for j in range(0,5):
        macierz[i,j]=list[licznik]
        licznik+=1

print(macierz)



