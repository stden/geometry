# -*- coding: utf-8 -*-

# Ответ 32 и все комбинации однозначно строятся из квадрата 3 на 2
N = 5
A = [([0] * N) for i in range(N)]


def check_sum(A, rows, cols):
    for i in range(len(A) - rows + 1):
        for j in range(len(A[0]) - cols + 1):
            s = 0
            for x in range(rows):
                for y in range(cols):
                    s += A[i + x][j + y]
            if (s % 2) != 0:
                return False
    return True


def check(A):
    return check_sum(A, 2, 3) and check_sum(A, 3, 2)


cnt = 0

assert check([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
assert check([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
assert check([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


def gen(A, i):
    global cnt
    if i == N * N:
        if check(A):
            cnt += 1
            print(cnt, A)
        return
    A[i / N][i % N] = 0
    gen(A, i + 1)
    A[i / N][i % N] = 1
    gen(A, i + 1)


#gen(A, 0)

#0001  1231
#0001  4562
#0001  631

#123
#456   0
#789

#7+8 чет
#8+9 чет
#7+9 чет


#000
#000

#7+8+9 = 0
#8+9 = 0
#7 = 0
#9 = 0

X = [[0,0,0],[0,0,0]]

# Общая сумма
s3 = sum(X[0][0:3],X[1][0:3]) % 2
print(s3)
s2 = sum([X[1][1],X[1][2]]) % 2
print(s2)
s1 = (s2+s3) % 2
print(s1)

# 2013
