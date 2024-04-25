x = int(input())
t = 0
c = 0 
r = 0 
s = 0
for i in range(0, x, 1):
    a, b = input().split()
    a = int(a)
    t = t + a
    if b == "C":
        c = c + a
    elif b == "R":
        r = r + a
    elif b == "S":
        s = s + a

print(f"Total: {t} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {100*c/t:.2f} %")
print(f"Percentual de ratos: {100*r/t:.2f} %")
print(f"Percentual de sapos: {100*s/t:.2f} %")