n = int(input())

for i in range(n):
    nome = input()
    notas = list(map(float, input().split()))
    if len(notas) == 1:
        print(f"{nome}: {notas[0]/2:.1f}")
    elif 2<= len(notas) <= 3:
        print(f"{nome}: {sum(notas)/len(notas):.1f}")
    elif len(notas) == 4:
        notas.sort()
        media = (notas[1] + notas[2] + notas[3])/3
        print(f"{nome}: {media:.1f}")