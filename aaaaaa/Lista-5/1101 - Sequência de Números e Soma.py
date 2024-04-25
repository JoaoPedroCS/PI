y = 0
while y == 0:
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        l = [a, b]
        l.sort()
        no = [x for x in range(l[0], l[1]+1, 1)]
        so = sum(no)
        print(*no, end=" ")
        print("Sum=", so, sep="")
    else:
        exit()