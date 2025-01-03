import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for data in data_set:
                file.write(f"{data}\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], [2, 3], 42)


class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        word = random.choice(self.words)
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Не знаю', 'Возможно')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
