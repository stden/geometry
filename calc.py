# coding=utf-8

# Демонстрация погрешности вычислений
a = 0.7
b = 0.6
c = 1.3
# С точки зрения математики 0.7 + 0.6 = 1.3
# Угадайте, что выведет следущая программа?
if a + b == c:
    print("YES!")
else:
    print("{0} + {1} != {2}".
          format(str(a), str(b), str(c)))

# >> Разбор формата представления чисел 
# с плавающей точкой в памяти (см. презентацию про формат чисел в памяти)
