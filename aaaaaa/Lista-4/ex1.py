#1043 - Triangle
a, b, c= map(float, input().split())
if a + b > c and a + c > b and c + b > a:
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {0.5 * (a + b)*c :.1f}")