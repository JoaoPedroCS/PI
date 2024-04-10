from typing import List
from math import pow

Mat = List[List[int]]
m = 24*60*60

def matrixMult(a: Mat, b: Mat) -> Mat:
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % m
    return result

def matrixPow(a: Mat, n: int) -> Mat:
    if n == 1:
        return a
    else:
        b = matrixPow(a, n // 2)
        c = matrixMult(b, b)
        if n % 2 == 0:
            return c
        else:
            return matrixMult(a, c)

def dabriel(n: int) -> int:
    x0 = [[1, 2]]
    a = [[1, 0], [1, 2]]
    xn = matrixMult(x0, matrixPow(a, n - 1))
    return xn[0][0]

n = int(input())
if n == 1:
    print("00:00:01")
else:
    x = dabriel(n)
    hours = x // 3600
    minutes = (x % 3600) // 60
    seconds = x % 60
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))