somatorio = []
for y in range(1, 11):
    hy = y**2 - 16
    if hy >= 0:
        fy = hy
    elif hy < 0:
        fy = 1
    
    if fy == 0:
        gy = y**2 + 16
    elif fy > 0:
        gy = 0

    conta = fy + gy
    somatorio.append(conta)
print(sum(somatorio))