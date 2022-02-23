import sys
import math

a = 'inżynieria systemów informatycznych'
print(type(a), "\n", a)


b = 5
print(type(b), "\n", b)


c = 5.1
print(type(c), "\n", c)


d = 2+3j
print(type(d), "\n", d)


# nowa_zmienna
# del a
# print(type(a), "\n", a)

f = 'isi'
g = 'grupa 3'

print(f+' '+g)

h = 7
i = 2
print(h // i)
print(2/4 ** i)
print(math.pow(2/4, i))

h += 1
print(h)

a = 5
b = 3
c = a - b
print("wynik działania %(z1)d - %(z2)d = %(z3)d" %{'z1':a, 'z2':b, 'z3':c})
print("wynik działania {0:d} - {1:d} = {2:d}".format(a, b, c))