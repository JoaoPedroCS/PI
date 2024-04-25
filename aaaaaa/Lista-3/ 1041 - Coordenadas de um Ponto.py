a, b = map(float, input().split())
if a>0:
    if b > 0:
        print("Q1")
    elif b < 0:
        print("Q4")
    else:
        print("Eixo X")
        
elif a < 0:
    if b > 0:
        print("Q2")
    elif b < 0:
        print("Q3")
    else:
        print("Eixo X")
        
elif a == 0 and b != 0:
    print("Eixo Y")
    
else:
    print("Origem")