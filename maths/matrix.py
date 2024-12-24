import numpy as np
import torch

# a = np.eye(5)
# b = np.ones((7, 5))
# c = np.full((5, 6), 7)
# d = np.random.random((5, 6))
# v = np.arange(0, 24, 2)
# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)
# print(v)
# d = v.reshape((3, 4))
# print(d)

# print(a[:, 1])


# print ("Вторая строка матрицы d:\n", d[1, :])
# print ("Четвертый столбец матрицы d:\n", d[:, 3])
# print ("Элементы матрицы d с координатами (1, 2) и (0, 3):\n", d[[1, 0], [2, 3]])


# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a.shape)
# b = a[:2, 1:3]
# print(b)
# print(a[0, 1])  # Prints "2"
# b[0, 0] = 77  # b[0, 0] is the same piece of data as a[0, 1]
# print(a[0, 1])


# Integer array indexing

# a = np.array([[1,2], [3, 4], [5, 6]])
# print(a)
# print()

# Пример Integer array indexing
# В результате получится массив размерности (3,)
# Обратите внимание, что до запятой идут индексы строк, после - столбцов
# print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
# print()

# По-другому пример можно записать так
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

np_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np_array)

torch_tensor = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(torch_tensor)

np_rand = np.random.rand(3,3)
print(np_rand)

torch_rand = torch.rand(3,3)
print(torch_rand)

np_zeros = np.zeros((3,3))
print(np_zeros)

torch_zeros = torch.zeros(3,3)
print(torch_zeros)

np_ones = np.ones((3,3))
print(np_ones)

torch_ones = torch.ones(3,3)
print(torch_ones)

np_id = np.identity(3)
print(np_id)

torch_id = torch.eye(3)
print(torch_id)