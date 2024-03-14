a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())


l = [a, b, c, d, e]
p = [x for x in l if x%2 == 0]
np = len(p)
print(f"{np:.0f} valores pares")
