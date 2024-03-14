while True:
    try:
        x, y, p = map(int, input().split())
        for i in range(p):
            a,b=map(int, input().split())
            if a<=x and b<=y or b<=x and a<=y:
                print("Sim")
            else:
                print("Nao")
    except:
        break