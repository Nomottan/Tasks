first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) for x, y in zip(first, second))
second_result = (True if len(first[x]) == len(second[x]) else False for x in range(0, len(first)))

print(list(first_result))
print(list(second_result))
