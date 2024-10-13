import io
from pprint import pprint


def custom_write(file_name, strings):
    strings_position = {}
    count = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        count += 1
        num_bite = file.tell()
        cords = (count, num_bite)
        strings_position[cords] = string
        file.write(f'{string}\n')
    file.close()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
