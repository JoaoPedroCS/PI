a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = [a, b, c, d, e]

e = [x for x in l if x%2 == 0]
o = [x1 for x1 in l if x1%2 != 0]
p = [x2 for x2 in l if 0 < x2]
n = [x3 for x3 in l if 0 > x3]
ne = len(e)
no = len(o)
np = len(p)
nn = len(n)
print(f"{ne} valor(es) par(es)")
print(f"{no:.0f} valor(es) impar(es)")
print(f"{np:.0f} valor(es) positivo(s)")
print(f"{nn:.0f} valor(es) negativo(s)")