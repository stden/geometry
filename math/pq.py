# -*- coding: utf-8 -*-

# p^2 - p + 1 = q^3, p,q - простые

# p^2 - p + 1 - q^3 = 0
# p^2 - 2p + 1 - p = q^3
# (p-1)^2 - (p - 1) - 1 = q^3

# p(p-1) = (q-1)(q^2 + q + 1)
# q-1 делится на p или на (p-1)
# 7              19 или на 18
# или 7^2 + 7 + 1 = 49 + 8 = 57  делится на p или на p-1

# p^2 - p + 1 - полный куб...
#


# p12 = (1 +- sqrt(1 - 4*(1 - q^3))) / 2
# 1 - 4*(1 - q^3) = 1 - 4 + 4q^3
# 4q^3 - 3
from math import sqrt

q = 7
for q in (range(2, 2000)):
    print(4 * q ** 3 - 3)
    print(sqrt(4 * q ** 3 - 3))

# 4*q**3 - 3 = l^2 - полный квадрат
# 4*q^3 - 3 = l^2
# (l^2 + 3) делится на 4

for l in range(100):
    if (l**2 + 3) % 4 == 0:
        print('l =',l)

print(4 * 7 ** 3, -3)

for p in range(2, 100):
    for q in range(2, 100):
        if p ** 2 - p + 1 == q ** 3:
            print(p, q)

# 2p = 1 + sqrt(-3 + 4q^3)

# p^2 - p + 1 = q^3, p,q - простые
# p(p-1) = q^3 - 1
p = 19
q = 7
print(p * (p - 1))
print(q ** 3 - 1)
print((q - 1) * (q ** 2 + q + 1))

# (q-1)*(q**2+q+1) : (p-1)
# q-1 : p-1
# q**2+q+1 : p-1
print(q ** 2 + q + 1, p)


# p^2 - p + 1
#
# q = 11


print(sqrt(4*q**3 - 3))

sqrs = [x**2 for x in range(2,10000)]
for q in range(2,200):
    res = 4*q**3 - 3
    if res in sqrs:
        print(q)

# 4*q**3 - 3 = l^2
# q**3 = (l^2 + 3)/4
# l^2 + 3 : q
#

q = 7
print(sqrt(4*q**3 - 3))
# 37


