import math
import matplotlib.pyplot as plt
import numpy


# Аппроксимация y(x) = a*(e^(b*x))
def approximate(nodes_x, nodes_y, x):
    # Выбрать наименьший положительный и неположительный y (для смещения)
    min_pos_y = min([element for element in nodes_y if element > 0])
    min_neg_y = min([element for element in nodes_y if element <= 0])
    print(min_pos_y, '   ', min_neg_y)

    # Временное смещение (log() не принимает в качестве аргумента отрицательные значения)
    print(nodes_y)
    for i in range(len(nodes_y)):
        nodes_y[i] += abs(min_neg_y) + 0.1
    print(nodes_y)

    # Линейная регрессия: заполнение СЛАУ
    n = len(nodes_x)
    matrix_a = [[0.0]*2]*2
    matrix_a[0][0] = n
    vector_b = [0.0] * 2

    for i in range(n):
        matrix_a[0][1] += nodes_x[i]  # x
        matrix_a[1][0] += nodes_x[i]  # x
        matrix_a[1][1] += nodes_x[i] ** 2  # x^2

        vector_b[0] += math.log(nodes_y[i])  # ln(y)
        vector_b[1] += math.log(nodes_y[i]) * nodes_x[i]  # ln(y)*x
    print(matrix_a)
    print(vector_b)


# Загрузка узловых точек из файла
f = open('nodes.in')
NodesX = []
NodesY = []
for line in f:
    NodesX.append(float(line.rstrip('\n').split(' ')[0]))
    NodesY.append(float(line.rstrip('\n').split(' ')[1]))

approximate(NodesX, NodesY, 3)

# Вычисление значения полинома в точках интерполяции
t = 0.001  # Отступ при вычислении новой точки
InterpolationX = []
InterpolationY = []
for f in numpy.arange(NodesX[0], NodesX[-1], t):
    InterpolationX.append(f)
    #InterpolationY.append(approximate(NodesX, NodesY, f))

