d, nd, m, nm = map(int, input().split())

if m%d != 0 or nd%m == 0:
    print("-1")
l = []
for j in range(2*d, m, d):
    if j%d == 0 and j%nd !=0 and m%j == 0 and nm%j != 0:
        l.append(j)
        
print(l)