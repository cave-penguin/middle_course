class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self.__color

    def __is_valid_sides(self, *args):
        return all(
            isinstance(side, int) and side > 0 and len(args) == self.sides_count
            for side in args
        )

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return int(sum(side) for side in self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [side for side in new_sides]


class Circle(Figure):
    sides_count = 1


class Triangle(Figure):
    pass


class Cube(Figure):
    pass
