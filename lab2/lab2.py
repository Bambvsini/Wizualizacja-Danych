# zad1
sporty = ['curling','bobsley','koszykowka','snooker']
sporty.reverse()
sporty.append('szachy')
print(sporty)

# zad2
slownik = {'Bibl':'Biblioteka', 'Arch':'Archiwum', 'Aten':'Ateneum'}
print(slownik['Bibl'])

#zad3
dict = {'Minecraft':'10', 'Terraira':'11', 'Limbo of The Lost':'galera'}
print (len(dict))
# Zadanie 4
napis = input("Wprowadz napis: ")
i=0
for x in napis:
    if x=='a':
        i+=1
print(i)
#zad5
import sys as system
system.stdout.write("Podaj pierwsza liczbe: ")
a = system.stdin.readline()
system.stdout.write("Podaj drugą liczbe: ")
b = system.stdin.readline()
system.stdout.write("Podaj trzecią liczbe: ")
c = system.stdin.readline()
a=int(a)
b=int(b)
c=int(c)
wynik=pow(a, b)+c
wynik=str(wynik)
system.stdout.write(wynik)
# Zadanie 6
a = input("/nPodaj pierwszą liczbę: ")
b = input("Podaj druga liczbę: ")
c = input("Podaj trzecią liczbę: ")

a=int(a)
b=int(b)
c=int(c)

if a>b and a>c:
    print(str(a) + " jest największa liczba")
if b>a and b>c:
    print(str(b) + " jest najwieksza liczba")
if c>a and c>b:
    print(str(c) + " jest najwieksza liczba")
import math
#zadanie 7
lista=[2, 3, 8.6, 3.2, 9, 8.4]
for x in lista:
    x=pow(x, 2)
    print(x)
#zadanie 8
i=0
lista2=[]
while(i<11):
    x=input("Podaj liczbe: ")
    x=int(x)
    if(x%2==0):
        lista2.append(x)
    i+=1
print(lista2)
#zadanie 9
a=input("Podaj liczbe")
a=int(a)
try:
    if (a<1):
        raise ValueError
    pierwiastek=math.sqrt(a)
    print(pierwiastek)
except ValueError:
    print("Podaj prawdiłową liczbe")