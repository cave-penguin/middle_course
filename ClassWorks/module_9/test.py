# def get_russian_name():
#     return ['Ваня', 'Коля', 'Маша']


# print(get_russian_name.__name__)
#
# my_func = get_russian_name
#
# print(my_func())
# print(my_func.__name__)

# def get_british_name():
#     return ['Oliver', 'Jack', 'Harry']
#
#
# name_getters = [get_russian_name, get_british_name]
#
# for name_getter in name_getters:
#     print(name_getter())

# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res
#
#
# def multiplier(args):
#     res = 1
#     for number in args:
#         res *= number
#     return res
#
#
# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f"Got {result}")
#
#
# my_numbers = [3, 2, 5, 6, 8, 1, 2, 4, 6]
#
# process_numbers(numbers=my_numbers, function=adder)
# process_numbers(numbers=my_numbers, function=multiplier)


# def mul_by_2(x):
#     return x * 2
#
#
# my_numbers = [3, 2, 5, 6, 8, 1, 2, 4, 6]
# my_numbers2 = [3, 2, 5, 6, 8, 1, 2, 4, 6]
#
# result = map(mul_by_2, my_numbers)
# result2 = map(lambda x, y: x * y, my_numbers, my_numbers2)
# print(result)
# print(list(result))
# print(result2)
# print(list(result2))


def is_odd(x):
    return x % 2


my_numbers = [3, 2, 5, 6, 8, 1, 2, 4, 6]

result = filter(is_odd, my_numbers)
result2 = filter(lambda x: x % 2, my_numbers)

print(result)
print(list(result))
print(result2)
print(list(result2))
