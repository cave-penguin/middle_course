from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(
            isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return all(isinstance(side, int) and side > 0 for side in args) and len(
            args) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != self.sides_count:
            self.set_sides(1)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != self.sides_count:
            self.set_sides(1, 1, 1)

    def get_square(self):
        a, b, c = self.get_sides()
        p = len(self) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            s = [sides[0] for _ in range(self.sides_count)]
            self.set_sides(*s)
        else:
            s = [1 for _ in range(self.sides_count)]
            self.set_sides(*s)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((0, 0, 0), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(triangle1.get_square())
triangle1.set_color(234, 123, 145)
print(triangle1.get_color())

triangle1.set_sides(5, 6, 7)
print(triangle1.get_sides())
print(triangle1.get_square())

print(circle1.get_square())
