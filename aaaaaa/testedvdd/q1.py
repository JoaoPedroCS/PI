n = int(input())

camisa_premiados = list(map(int, input().split()))
fabricadas_p = int(input())
fabricadas_m = int(input())
no_de_p = 0
no_de_m = 0

for i in range(n): 
    if camisa_premiados[i] == 1:
        no_de_p += 1
    elif camisa_premiados[i] == 2:
        no_de_m += 1


if n != fabricadas_p + fabricadas_m or n != len(camisa_premiados):
    print("N")

elif no_de_p == fabricadas_p and no_de_m == fabricadas_m:
    print("S")

else:
    print("N")