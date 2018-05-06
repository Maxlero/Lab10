"""
    Автор: Орел Максим
    Группа: КБ-161
    Вариант: 11 (task 1: var 2; task 2: var 11)
    Дата создания: 6/05/2018
    Python Version: 3.6
"""
import matplotlib.pyplot as plt
import numpy as np

# http://mathprofi.ru/metod_prjamougolnikov.html
# http://mathprofi.ru/formula_simpsona_metod_trapecij.html


a = -1
b = 2
h = 0.1
h2 = [2, 4, 6, 8, 10, 10000]


def pauline(point):
    return 1 + 0.9 * point + 0.8 * point ** 2 + 0.7 * point ** 3 + 0.5 * point ** 4


def rectangle_left(left, right):
    return (right - left) * pauline(left)


def rectangle_right(left, right):
    return (right - left) * pauline(right)


def trapeze(left, right):
    return (right - left) / 2 * (pauline(left) + pauline(right))


def simpson(left, right):
    return (right - left) / 6 * (pauline(left) + 4 * pauline((left + right) / 2) + pauline(right))


def f(point):
    return (2 * point) ** 3 * np.cos(point)


def trapeze2(left, right):
    return (right - left) / 2 * (f(left) + f(right))


def simpson2(left, right):
    return (right - left) / 6 * (f(left) + 4 * f((left + right) / 2) + f(right))


def sum(coef, left, right):
    return_sum = 0
    for i in coef:
        return_sum += f((right + left) / 2 + ((right - left) / 2) * i)
    return return_sum


if __name__ == "__main__":
    try:
        x = np.linspace(a, b)
        plt.plot(x, pauline(x))
        plt.grid()
        plt.show()

        # task 1
        print('Метод левого прямоугольника: {0}'.format(rectangle_left(a, b)))
        print('Метод правого прямоугольника: {0}'.format(rectangle_right(a, b)))
        print('Метод трапеции: {0}'.format(trapeze(a, b)))
        print('Метод Симпсона: {0}'.format(simpson(a, b)))

        points = np.arange(a, b + h, h)
        A = [0, 0, 0, 0]
        for i in range(0, len(points) - 1):
            A[0] += rectangle_left(points[i], points[i + 1])
            A[1] += rectangle_right(points[i], points[i + 1])
            A[2] += trapeze(points[i], points[i + 1])
            A[3] += simpson(points[i], points[i + 1])

        print('Метод левого прямоугольника (обобщённый): {0}'.format(A[0]))
        print('Метод правого прямоугольника (обобщённый): {0}'.format(A[1]))
        print('Метод трапеции (обобщённый): {0}'.format(A[2]))
        print('Метод Симпсона (обобщённый): {0}'.format(A[3]))

        # task 2
        x = np.linspace(a, b)
        plt.plot(x, f(x))
        plt.grid()
        plt.show()

        print()
        for k in h2:
            h = (b - a) / k
            points = np.arange(a, b + h, h)
            A = [0, 0]
            for i in range(0, len(points) - 1):
                A[0] += trapeze2(points[i], points[i + 1])
                A[1] += simpson2(points[i], points[i + 1])
            print('Метод трапеций (h = (b-a)/{0}): {1}'.format(k, A[0]))
            print('Метод Симпсона (h = (b-a)/{0}): {1}'.format(k, A[1]))
            print()

        coef = [0.707197, 0, -0.707197]
        answer = sum(coef, a, b) * (b - a) / 3
        print('Чебышев (n = 3):', answer)

        coef = [0.794654, 0.187592, -0.187592, -0.794654]
        answer = sum(coef, a, b) * (b - a) / 4
        print('Чебышев (n = 4):', answer)

        coef = [0.832498, 0.374541, 0, -0.374541, -0.832498]
        answer = sum(coef, a, b) * (b - a) / 5
        print('Чебышев (n = 5):', answer)

        # answer must be near -2.44

    except Exception as e:
        print(e)
