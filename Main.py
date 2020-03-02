import math
import matplotlib.pyplot as plt
import numpy
import LinearEquations


# Аппроксимация y(x) = a*(e^(b*x))
def approximate(nodes_x, nodes_y):
    # Выбрать наименьший положительный и неположительный y (для смещения)
    min_pos_y = min([element for element in nodes_y if element > 0])
    min_neg_y = min([element for element in nodes_y if element <= 0])

    # Временное смещение (log() не принимает в качестве аргумента отрицательные значения)
    for i in range(len(nodes_y)):
        nodes_y[i] += abs(min_neg_y) + 0.1

    # Линейная регрессия: заполнение СЛАУ
    n = len(nodes_x)
    matrix_a = [[0] * 2 for i in range(2)]
    matrix_a[0][0] = n
    vector_b = [0.0] * 2

    # Заполняем матрицу значениями линеаризованного уравнения
    for i in range(n):
        matrix_a[0][1] += nodes_x[i]  # x
        matrix_a[1][0] += nodes_x[i]  # x
        matrix_a[1][1] += nodes_x[i] ** 2  # x^2

        vector_b[0] += math.log(nodes_y[i])  # ln(y)
        vector_b[1] += math.log(nodes_y[i]) * nodes_x[i]  # ln(y)*x

    # Находим решение СЛАУ линейной регрессии любым удобным методом
    gauss_sol = LinearEquations.gauss(matrix_a, vector_b)

    # Находим точки аппрокисмации
    t = 0.001  # Отступ при вычислении новой точки
    interpolation_x = []
    interpolation_y = []
    for x in numpy.arange(NodesX[0], NodesX[-1], t):
        interpolation_x.append(x)
        interpolation_y.append(math.exp(gauss_sol[0]) * math.exp(gauss_sol[1] * x) - abs(min_neg_y) - 0.1)  # e^a * e^bx + смещение

    # График в matplotlib
    fig = plt.figure()
    # Описания к графику
    plt.title('Approximation y(x) = a*e^bx')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    # Построение точечного графика
    plt.scatter(NodesX, NodesY, color='red')
    # Построение графика интерполяции
    plt.plot(interpolation_x, interpolation_y)
    # Вывод графика в IDE
    plt.show()
    # Сохранение в png
    fig.savefig('Approximation.png')


# Загрузка узловых точек из файла
f = open('nodes.in')
NodesX = []
NodesY = []
for line in f:
    NodesX.append(float(line.rstrip('\n').split(' ')[0]))
    NodesY.append(float(line.rstrip('\n').split(' ')[1]))

# Аппроксимация
approximate(NodesX, NodesY)


