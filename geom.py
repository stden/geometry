# -*- coding: utf-8 -*-
# Часто используемые геометрические операции


# Импортируем все функции из math
from math import *
# math.sqrt()... sqrt()

class Point:  # Класс "Точка", этот же класс используется как Вектор
    x, y = 0, 0

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(A, B):
        return Point(A.x + B.x, A.y + B.y)

    def __sub__(A, B):
        return Point(A.x - B.x, A.y - B.y)


def dist(A, B):  # Расстояние между точками
    return sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)


# Проверка работы функции
# assert - проверка утверждения, если утверждение не верно,
# то генерируется ошибка выполнения
assert dist(Point(1, 0), Point(3, 0)) == 2


# Скалярное произведение векторов
def scalar(A, B):
    return A.x * B.x + A.y * A.y


# Векторное произведение векторов
# Используется, например, для вычисления площади произвольного многоугольника,
# определения "левых" поворотов при построении выпуклой оболочки и т.д.
def cross_product(A, B):
    return A.x * B.y - A.y * B.x


A, B = Point(), Point()
A.x, A.y, B.x, B.y = 1, 2, 3, 4

# print(A, B, dist(A, B), scalar(A, B), cross_product(A, B))

# Целые числа из файла
def readInts():
    if sys.version < '3': # for Python 2
        return [int(x) for x in raw_input().split()]
    return [int(x) for x in input().split()]


class Line:  # Класс "Прямая"
    a, b, c = 0, 0, 0

    def __init__(x, a, b, c):
        x.a, x.b, x.c = a, b, c


def solve(a1, b1, c1,
          a2, b2, c2):
    """
       Общение решение системы линейных уравнений по методу Крамера
       (в неоднородных декартовых координатах или просто произвольных уравнений)
    """
    d = a1 * b2 - b1 * a2
    dx = c1 * b2 - b1 * c2
    dy = a1 * c2 - c1 * a2
    if d == 0:
        if dx == 0 and dy == 0:
            return "Любое решение"
        else:
            return "Нет решений"
    x = dx / float(d) # Деление в целых числах будет ошибкой
    y = dy / float(d) # и потому надо привести делитель к float()
    assert a1 * x + b1 * y == c1
    assert a2 * x + b2 * y == c2

    return x, y


p1 = Point(2, 3)


import sys

sys.stdin = open("lines.in", "r")
# sys.stdout = open("lines.out", "w")

# Читаем исходные данные
# Первый отрезок
A, B = Point(), Point()
A.x, A.y, B.x, B.y = readInts()

# Второй отрезок
C, D = Point(), Point()
C.x, C.y, D.x, D.y = readInts()

AB = B - A
CD = D - C
AC = C - A
print(A, B, AB)

# Пересечение двух отрезков
# Векторное уравнение: A + AB * t = C + CD * q
# AB * t - CD * q = C - A
# t,q in [0,1]

# По координатам:
# AB.x * t - CD.x * q = C.x - A.x
# AB.y * t - CD.y * q = C.y - A.y

res = solve(AB.x, CD.x, C.x - A.x,
            AB.y, CD.y, C.y - A.y)

if len(res) == 2:
   t, q = res
   print(A.x + AB.x * t, A.y + AB.y * t)
else:
   print(-1)




def lineByPoints(A, B):  # Прямая по 2-м точкам
    l = Line(0, 0, 0)

    d = A.x * B.y - A.y * B.x  # Общий определитель
    dA = A.y - B.y  # Определитель a
    dB = A.x - B.x  # Определитель b
    # Прямые параллельны или на одной прямой
    # if d == 0:
    # if dA == 0 and dB == 0:


    l.a = dA / d
    l.b = dB / d
    l.c = - l.a * A.x - l.b * A.y
    # Проверяем ответ
    assert l.a * A.x + l.b * A.y + l.c == 0
    assert l.a * B.x + l.b * B.y + l.c == 0
    # Возвращаем ответ
    return l


    # l1 = lineByPoints(A, B)
    # l2 = lineByPoints(C, D)