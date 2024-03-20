i = 2520
l = [3,6,7,8,9,11,12,13,14,15,16,17,18,19]
while True:
    contagem = 0
    for d in l:
        if i % d == 0: 
            contagem += 1
        elif i % d != 0:
            break
    if contagem >=14:
        print(i, contagem)
        x = 0
        break
    elif contagem < 14:
        i += 20
print("terminou")