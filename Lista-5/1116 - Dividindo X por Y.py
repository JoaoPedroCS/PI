n = int(input())

for i in range(0, n, 1):
    a, b = map(int, input().split())
    if b == 0:
        print("divisao impossivel")
    else:
        print(round(a/b, 1))