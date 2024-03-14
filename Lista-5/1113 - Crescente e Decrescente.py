a, b = map(int, input().split())
while a != b:
    try:
        if a > b:
            print("Decrescente")
        elif a < b:
            print("Crescente")
        a, b = map(int, input().split())
    except EOFError:
        break