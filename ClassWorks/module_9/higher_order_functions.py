# def multiplier_v1(n):
#     if n == 2:
#         def multiplier(x):
#             return x * 2
#
#     elif n == 3:
#         def multiplier(x):
#             return x * 3
#
#     else:
#         raise Exception('Я могу сделать умножители только на 2 или 3')
#
#     return multiplier
#
#
# numbers = [2, 6, 5, 3, 4, 7, 8, 1]
#
# by_2 = multiplier_v1(2)
# by_3 = multiplier_v1(3)
#
# result = map(by_2, numbers)
# print(list(result))
# result = map(by_3, numbers)
# print(list(result))
# from pprint import pprint


# def multiplier_v2(n):
#     if n in {2, 3}:
#         return lambda x: x * n
#     raise Exception('Я могу сделать умножители только на 2 или 3')
#
# result_by_2 = [by_2(x) for x in numbers]
# result_by_3 = [by_3(x) for x in numbers]
#
# print(result_by_2)
# print(result_by_3)

# def get_multiplier_v2(n):
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
#
# by_5 = get_multiplier_v2(5)
# print(by_5(x=42))

# numbers = [2, 6, 5, 3, 4, 7, 8, 1]
#
# by_10 = get_multiplier_v2(10)
# by_100 = get_multiplier_v2(100)
#
# print(list(map(by_10, numbers)))
# print(list(map(by_100, numbers)))

# def matrix(some_list):
#     def multiply_column(x):
#         res = []
#         for elem in some_list:
#             res.append(elem * x)
#         return res
#
#     return multiply_column
#
#
# numbers = [2, 6, 5, 3, 4, 7, 8, 1]
# numbers2 = [8, 2, 3, 6, 1, 0, 7, 9]
#
# matrix_on_my_numbers = matrix(numbers)
# result = map(matrix_on_my_numbers, numbers2)
# pprint(list(result))
# # danger!!! it would be a mistake
# numbers.extend([10, 20, 30])
# result = map(matrix_on_my_numbers, numbers2)
# pprint(list(result))

class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n


numbers = [2, 6, 5, 3, 4, 7, 8, 1]

by_100500 = Multiplier(n=100500)
result = by_100500(x=42)
print(result)

result = map(by_100500, numbers)
print(list(result))
