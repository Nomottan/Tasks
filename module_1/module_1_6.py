#Задание 1
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Словарь: ', my_dict)
print('Существующее значение: ', my_dict['Vasya'])
print('Несуществующее значение: ', my_dict.get('Vova'))
my_dict.update({'Vova': 1994,
                'Lena': 1985})
del_val = my_dict.pop('Egor')
print('Удаленное значение: ', del_val)
print('Измененный словарь: ', my_dict)

#Задание 2
my_set = {1, 3, 8, 3, 1, 7, 'String', False, True, 0}
print('Множестово: ', my_set)
my_set.add('ок')
my_set.add('да')
my_set.remove(False)
print('Измененное множество: ', my_set)