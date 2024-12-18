from pprint import pprint

name = 'sample.txt'
text = 'Hello, my darling'
file = open(name, 'r', encoding='utf-8')
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()
