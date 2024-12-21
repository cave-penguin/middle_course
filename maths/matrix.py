import numpy as np

# a = np.eye(5)
# b = np.ones((7, 5))
# c = np.full((5, 6), 7)
# d = np.random.random((5, 6))
v = np.arange(0, 24, 2)
# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)
print(v)
s = v.reshape((3, 4))
print(s)

# print(a[:, 1])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a.shape)
b = a[:2, 1:3]
print(b)
print(a[0, 1])  # Prints "2"
b[0, 0] = 77  # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])
