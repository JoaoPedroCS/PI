#1045 - Triangle Types
x, y, z= map(float, input().split())
l = [x, y, z]
l.sort(reverse=True)
a, b, c = l[0], l[1], l[2]
if a>=b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2+c**2:
        print("TRIANGULO RETANGULO")
    elif a**2>b**2+c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2<b**2+c**2:
        print("TRIANGULO ACUTANGULO")
            
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a==b != c or a==c != b or b==c != a:
        print("TRIANGULO ISOSCELES")