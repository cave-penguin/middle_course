def validate(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return False
    return isinstance(a, (int, float, str)) and isinstance(b, (int, float, str))


def add_everything_up(a, b):
    if validate(a, b):
        try:
            return round(a + b, 3)
        except TypeError:
            return f"{a}{b}"
    else:
        return "Wrong types"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
