a = [1, 4, 2, 3, 6, 7, 8, 0]
b = [3, 2, 3, 6, 7, 8, 9, 1, 2, 0]

# list1 = [x * y for x in range(5) for y in range(5, 10)]
# print(list1)
# list2 = [x * 2 if x > 3 else x * 3 for x in range(7)]
# print(list2)
# list3 = [x * y for x in a for y in b if x % 2 and y // 2]
# print(list3)

dict_ = {x: x ** 2 for x in a}
print(dict_)

set_ = {x for x in b}
print(set_)
