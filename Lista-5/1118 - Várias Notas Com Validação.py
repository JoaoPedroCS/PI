y = 0
x = 0
z = True
while True:
    z = True
    a = float(input())
    if a < 0 or a > 10:
        print("nota invalida")
    else:
        x += a
        y += 1
    if y == 2:
        print(f"media = {x/2:.2f}")
        while z:
            reset = input(f"novo calculo (1-sim 2-nao)\n")
            if reset == "1":
                y = 0
                x = 0
                z = False
            elif reset == "2":
                exit()