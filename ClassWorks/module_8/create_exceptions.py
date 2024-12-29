# def greet_person(name):
#     if name == 'ВоланДеМорт':
#         raise Exception(f'We dont love you, {name}')
#     print(f'Hello {name}')
#
#
# greet_person('Micky')
# greet_person('ВоланДеМорт')


# try:
#     raise NameError("Hello there")
# except NameError as exc:
#     print(f"Exception type {type(exc)} flew past! Its parameters {exc.args}")
#     raise


# class ProZero(Exception):
#     pass
#
#
# def f(a, b):
#     if b == 0:
#         raise ProZero("Деление на ноль невозможно")
#     return a / b


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero("Деление на ноль невозможно", {'a': a, 'b': b})
    return a / b


try:
    result = f(10, 0)
    print(result)
except ProZero as e:
    print("Не очень хороший день, мы словили ошибку")
    print(f"Сообщение об ошибке: {e.message}")
    print(f"Дополнительная информация: {e.extra_info}")
