#1060 - Positive Numbers
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

l = [a, b, c, d, e, f]
p = [x for x in l if x > 0]
np = len(p)
print(f"{np} valores positivos")