try: 
    a, b = map(int, input().split())
    while True:
        if a == 0 or b == 0:
            exit()
        else:
            if a > 0 and b > 0:
                print("primeiro")
            elif a < 0 and b > 0:
                print("segundo")
            elif a < 0 and b < 0:
                print("terceiro")
            elif a > 0 and b < 0:
                print("quarto")
        a, b = map(int, input().split())
except ValueError:
    exit()
