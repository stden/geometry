# -*- coding: utf-8 -*-
# Операции в однородных координатах

from fractions import *

print(gcd(10, 5))


class Point:  # Класс "Точка" (вектор) с однородными координатами
    x, y, w = 0, 0, 1

    # Конструктор
    def __init__(self, x=0, y=0):
        self.x, self.y, self.w = x, y, 1

    # Строка для вывода
    def __repr__(x):
        return "(" + str(x.x / float(x.w)) + \
               "," + str(x.y / float(x.w)) + ")"

    # Сложение векторов
    def __add__(A, B):
        R = Point()
        R.w = B.w * A.w
        R.x = A.x * B.w + B.x * A.w
        R.y = A.y * B.w + B.y * A.w
        # Если вычисление идёт в целых числах,
        # то можно дроби сократить на НОД
        # Сокращаем дроби чтобы работать с целыми числами в меньшем диапазоне
        # Проверяем что числа целые.
        # Если изначально даны координаты в целых числах, то они и будут оставаться
        # целыми до момента вывода или до операции с результатом
        # в действительных числах, например, извлечения корня
        if (type(R.x) is int) and (type(R.y) is int) and (type(R.w) is int):
            common_gcd = gcd(gcd(R.x, R.y), R.w)  # Общий НОД
            R.x /= common_gcd  # Делим x на НОД
            R.y /= common_gcd  # Делим y на НОД
            R.w /= common_gcd  # Делим Вес на НОД
        return R

    # Вычитание векторов
    def __sub__(A, B):
        res = Point()
        res.w = B.w * A.w
        res.x = A.x * B.w - B.x * A.w
        res.y = A.y * B.w - B.y * A.w
        return res

    # Разделить вектор на число (масштабирование)
    def __div__(A, x):
        res = Point()
        res.x = A.x
        res.y = A.y
        res.w = A.w * x
        return res


# Заведём 2 точки
A = Point(2, 10)
print(A)
B = Point(3, 5)
print(B)
AB = B - A
print(AB)
AB2 = AB / 3
print(AB2.x, AB2.y, AB2.w)
v = Point(3, 2)
AB2 = AB2 - v
print(AB2.x, AB2.y, AB2.w)
print(AB2)

# Скалярное произведение в однородных координатах
def scalar(A, B):
    # A.x * B.x + A.y * B.y
    return (A.x * B.x + A.y * B.y) / float(A.w * B.w)


v1 = Point(5, 5)
v2 = Point(-5, 5)
print("Скалярное произведение: %d" % scalar(v1, v2))


def solve(a1, b1, c1,
          a2, b2, c2):
    """
       Общение решение системы линейных уравнений по методу Крамера
       Для получения решения в однородных координатах
    """
    d = a1 * b2 - b1 * a2
    x = c1 * b2 - b1 * c2
    y = a1 * c2 - c1 * a2
    if d == 0:
        if x == 0 and y == 0:
            return "Любое решение"
        else:
            return "Нет решений"
    assert a1 * x + b1 * y == c1 * d
    assert a2 * x + b2 * y == c2 * d

    return x, y, d


class Line:  # Класс "Прямая" (тоже в однородных коодинатах)
    a, b, c = 0, 0, 0

    def __init__(x, a, b, c):
        x.a, x.b, x.c = a, b, c


l1 = Line(1, 0, 0)

l2 = Line(a=0, b=1, c=-1)

print(solve(l1.a, l1.b, l1.c,
            l2.a, l2.b, l2.c))

x, y, w = 2, 3, 3
print(x, y, w)
x, y = x / float(w), y / float(w)
print(x, y)
