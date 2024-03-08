#1046 - Game Time
a, b= map(int, input().split())
if a==b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    if b>a:
        print(f"O JOGO DUROU {b-a} HORA(S)")
    else:
        print(f"O JOGO DUROU {(24-a)+b} HORA(S)")
