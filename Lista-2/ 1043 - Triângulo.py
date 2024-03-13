a, b, c = list(map(float, input().split()))
l = [a, b, c]
l.sort()
if l[0] + l[1] > l[2]:
    print(f"Perimetro = {l[0]+l[1]+l[2]:.1f}")
else:
    print(f"Area = {(a*c/2)+(b*c/2):.1f}")