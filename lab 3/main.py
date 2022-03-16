import math
import random
a = [1-x for x in range(1, 11)]
b = [4**x for x in range (0, 8)]
c = [x for x in b if x%2==0]
print(a)
print(b)
print(c)
#zad2
random.seed(a=None, version=2)
rand=[]
for x in range(0, 10):
    rand.append(math.floor(random.random()*100))
print(rand)
brand = [x for x in a if x%2==0]
print(brand)
#zad3
prod = {'mleko':'litry', 'bułki':'sztuki', 'ziemniaki':'kilogramy'}
prod_b =  [x for x in prod if prod[x]=='sztuki']
print(prod_b)
#zad4
def czy_prostokatny(a, b, c):
    if a**2 + b**2 == c**2:
        return 'prostokatny'
    else:
        return 'nie prostokatny'
print(czy_prostokatny(6, 8, 10))
#zad5
def pole_trapezu(a = 1, b = 2, h =3):
    pole = ((a + b) * h) / 2
    return pole
print(pole_trapezu())
print(pole_trapezu(2, 4, 6))
#zad6
def iloczyn_ciagu(a = 1, b = 4, c = 10):
    for x in range(c):
        a*=b
    return a
print(iloczyn_ciagu())
#zad7
def iloczyn_ciagu2(*a)
    if len(a)==0:
        return 0
    else:
        iloczyn = 1
        for x in liczba:
            iloczyn*=x
        return iloczyn
print(iloczyn_ciagu2(1,2,3,4,5))
#zadanie 8
