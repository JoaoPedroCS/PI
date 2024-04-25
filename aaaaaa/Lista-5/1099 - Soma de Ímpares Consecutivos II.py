x = int(input())

for i in range(0, x, 1):
    a, b = map(int, input().split())
    l = [a, b]
    l.sort()
    no = [x for x in range(l[0]+1, l[1], 1) if x%2 != 0]
    so = sum(no)
    print(so)