lmt = int(600851475143/2) +1
l = [0]
for i in range(2, lmt):
    div = 1
    for x in range(1, i):
        if i%x == 0:
            div += 1
    if div == 2:
        l.append(i)

print(l)