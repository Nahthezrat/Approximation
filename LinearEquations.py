# Перемена местами двух строк системы
def swap_rows(matrix_a, vector_b, row1, row2):
    matrix_a[row1], matrix_a[row2] = matrix_a[row2], matrix_a[row1]
    vector_b[row1], vector_b[row2] = vector_b[row2], vector_b[row1]


# Деление строки системы на число
def divide_row(matrix_a, vector_b, row, divider):
    matrix_a[row] = [a / divider for a in matrix_a[row]]
    vector_b[row] /= divider


# Сложение строки системы с другой строкой, умноженной на число
def combine_rows(matrix_a, vector_b, row, source_row, weight):
    matrix_a[row] = [(a + k * weight) for a, k in zip(matrix_a[row], matrix_a[source_row])]
    vector_b[row] += vector_b[source_row] * weight


# Решение СЛАУ методом Гаусса (приведением к треугольному виду)
def gauss(matrix_a, vector_b):
    column = 0
    while column < len(vector_b):

        # Ищем максимальный по модулю элемент в столбце
        current_row = None
        for r in range(column, len(matrix_a)):
            if current_row is None or abs(matrix_a[r][column]) > abs(matrix_a[current_row][column]):
                current_row = r
        if current_row is None:
            print("No solutions")
            return None

        if current_row != column:
            # Переставляем строку с найденным элементом выше
            swap_rows(matrix_a, vector_b, current_row, column)

        # Нормализуем строку с найденным элементом
        divide_row(matrix_a, vector_b, column, matrix_a[column][column])

        # Обрабатываем нижележащие строки
        for r in range(column + 1, len(matrix_a)):
            combine_rows(matrix_a, vector_b, r, column, -matrix_a[r][column])

        column += 1

    # Матрица приведена к треугольному виду, считаем решение
    vector_x = [0 for b in vector_b]
    for i in range(len(vector_b) - 1, -1, -1):
        vector_x[i] = vector_b[i] - sum(x * a for x, a in zip(vector_x[(i + 1):], matrix_a[i][(i + 1):]))

    # Возвращаем ответ
    return vector_x
