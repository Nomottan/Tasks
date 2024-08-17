def get_matrix(n, m, value): #Решение задачи
    if n == 0 or m == 0:
        return ("Недопустимые параметры матрицы")
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for c in range(0, m):
            matrix[i].append(value)
    return (matrix)

def matrix_print(result): #Чисто для себя чтоб разобраться, построчный вывод ответа
    for x in range(0, len(result)):
        row = result[x]
        print(row)
    print(f'\n')
    return


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

matrix_print(result1)
matrix_print(result2)
matrix_print(result3)


