i = 2520
l = [19, 17, 15, 13, 11, 9, 7, 3, 18, 16, 14, 12, 8, 6]
while True:
    contagem = 0
    for d in l:
        if i % d == 0: 
            contagem += 1
        elif i % d != 0:
            break
    if contagem >=14:
        print(i, contagem)
        break
    elif contagem < 14:
        i += 20
print("end")