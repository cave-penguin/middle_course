def greet_person(name):
    if name == 'ВоланДеМорт':
        raise Exception(f'We dont love you, {name}')
    print(f'Hello {name}')

greet_person('ВоланДеМорт')
greet_person('Micky')