# zad 1

# a = np.arange(3)
# b = np.arange(3)
# print(a*b)
#
# # zad 2
#
# a = np.arange(9).reshape(3,3)
# b = np.arange(16).reshape(4,4)
# print(a)
# print(b)
# print()
# print(a.min(axis = 0))
# print(a.min(axis = 1))
# print()
# print(b.min(axis = 0))
# print(b.min(axis = 1))
#
# # zad 3
#
# a = np.arange(3)
# b = np.arange(3)
# c = a.dot(b)
# print(c)
#
# # zad 4
#
# a = np.array([2, 4, 5])
# b = np.array([2.5, 3.2, 1.5])
# print(a*b)

# zad 5

b = np.arange(6).reshape(2,3)
print(b)
c=np.sin(b)
print(np.sin(b))


# # zad 6

a = np.arange(6).reshape(2,3)
print(a)

b = np.cos(a)
print(b)

# zad 7

print(c+b)

# zad 8
a=np.arange(9).reshape(3,3)
for b in a:
    print(b)

# zad 9
a=np.arange(9).reshape(3,3)
for b in a.flat:
    print(b)

# zad 10
a=np.arange(81).reshape(9,9)
print('normalnie')
print(a)
print('ravel')
b=a.ravel()
print(b)
print('T')
c=a.T
print(c)
a=np.arange(81).reshape(81,1)
print('normalnie')
print(a)
print('ravel')
b=a.ravel()
print(b)
print('T')
c=a.T
print(c)
a=np.arange(81).reshape(3,27)
print('normalnie')
print(a)
print('ravel')
b=a.ravel()
print(b)
print('T')
c=a.T
print(c)
a=np.arange(81).reshape(27,3)
print('normalnie')
print(a)
print('ravel')
b=a.ravel()
print(b)
print('T')
c=a.T
print(c)
a=np.arange(81)
print('normalnie')
print(a)
print('ravel')
b=a.ravel()
print(b)
print('T')
c=a.T
print(c)
# # zad 11

a=np.arange(12)
b=a.reshape(3,4)
print("3x4")
print(b)
print('')
c=a.reshape(4,3)
print("4x3")
print(c)
print('')
d=a.reshape(2,6)
print("2x6")
print(d)
print('')
print("3x4-flat")
print(b.ravel())
print('')
print("4x3-flat")
print(c.ravel())
print('')
print("2x6-flat")
print(d.ravel())
print('')
