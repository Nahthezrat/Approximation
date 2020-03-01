import math
import matplotlib.pyplot as plt
import numpy
import LinearEquations


# Аппроксимация y(x) = a*(e^(b*x))
def approximate(nodes_x, nodes_y):
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

    soluton = LinearEquations.linearsolver(matrix_a, vector_b)

    # Вычисление значения полинома в точках интерполяции
    t = 0.001  # Отступ при вычислении новой точки
    InterpolationX = []
    InterpolationY = []
    for x in numpy.arange(NodesX[0], NodesX[-1], t):
        InterpolationX.append(x)
        InterpolationY.append(math.exp(soluton[0]) * (math.exp(soluton[1]*x)) - abs(min_neg_y + 0.1)) # e^a * bx

    # График в matplotlib
    fig = plt.figure()
    # Описания к графику
    plt.title('Newton-1 Interpolation')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    # Построение точечного графика
    plt.scatter(NodesX, NodesY, color='red')
    # Построение графика интерполяции
    plt.plot(InterpolationX, InterpolationY)
    # Вывод графика в IDE
    plt.show()
    # Сохранение в png
    fig.savefig('NewtonInterpolation.png')

# Загрузка узловых точек из файла
f = open('nodes.in')
NodesX = []
NodesY = []
for line in f:
    NodesX.append(float(line.rstrip('\n').split(' ')[0]))
    NodesY.append(float(line.rstrip('\n').split(' ')[1]))

approximate(NodesX, NodesY)
