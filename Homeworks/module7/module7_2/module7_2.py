def custom_write(file_name, strings):
    position = {}
    str_num = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        cursor = file.tell()
        file.write(f"{string}\n")
        str_num += 1
        position[(str_num, cursor)] = string
    file.close()
    return position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

name = "sample.txt"

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
