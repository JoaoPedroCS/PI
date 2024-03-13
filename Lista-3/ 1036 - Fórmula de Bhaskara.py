a, b, c = map(float, input().split())
if a == 0 or b*b-4*a*c < 0:
    print("Impossivel calcular")
else:
    d = (b*b-4*a*c)**0.5
    r1 = (-b+d)/(2*a)
    r2 = (-b-d)/(2*a)
    print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")