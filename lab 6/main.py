import numpy as np

a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)

print(type(a))

print(a.dtype)

a = np.arange(2, dtype='int64')
print(a.dtype)

b = a.astype('float')
print(b)
print(b.dtype)

print(b.shape)

print(a.ndim)

m = np.array([np.arange(2), np.arange(2)])
print(m.shape)

print(type(m))


zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera)
print(jedynki)

print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2))
print(pusta)

poz_1=pusta[1,1]
poz_2=pusta[0,1]
print(poz_1)
print(poz_2)

macierz = np.array([[1,2], [3,4]])
print(macierz)

liczby = np.arange(1, 2, 0.1)
print(liczby)

liczby_lin = np.linspace(1, 2, 5)
print(liczby_lin)

z = np.indices((5,3))
print(z)

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

mat_diag_k = np.diag([a for a in range(5)], -1)
print(mat_diag_k)

z = np.fromiter(range(5), dtype='int32')
print(z)

test = b'Test'
#Tes = np.frombuffer(Test, dtype='S1')
#print(Tes)
#Tes_2 = np.frombuffer(Test, dtype='S2')
#print(Tes_2)

test = 'Test'
tes_3 = np.array(list(test))
tes_4 = np.array(list(test), dtype='S1')
tes_5 = np.array(list(b'Test'))
tes_6 = np.fromiter(test, dtype='S1')
tes_7 = np.fromiter(test, dtype='U1')
print(tes_3)
print(tes_4)
print(tes_5)
print(tes_6)
print(tes_7)


mat = np.ones((2,2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat*mat_1)
print(mat/mat_1)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])


print(a[2:7:2])

print(a[1:])
print(a[2:5])

mat = np.arange(25)

mat = mat.reshape((5,5))
print(mat)
print(mat[1:])
print(mat[:,1])
print(mat[:, -1:])
print(mat[2:6, 1:3]
print(mat[:, range(2, 6, 2)])
print('')

 
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)
