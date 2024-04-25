a = input().split(" ", 3)

i = a[0]
r = float(a[1])
c = a[2]
f = a[3]

print(f"{i}{r:.6f}{c}{f}")
print(f"{i}\t{r:.6f}\t{c}\t{f}")
print(f"{i:.10s}{r:10.6f}{c:10s}{f:10s}")
