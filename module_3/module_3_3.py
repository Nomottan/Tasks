def print_params(a=1, b='строка', c=True):
    print(f'Параметры: a = {a}, b = {b}, c = {c}')
    return

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['строка 2', False, 37]
values_dict = {'a': True, 'b': 12, 'c': 'строка 3'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 12]

print_params(*values_list_2, 42)