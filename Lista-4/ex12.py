#1061 - Event Time
dd = input().split("Dia ")
h, m, s = map(int, input().split(" : "))
dd1 = input().split("Dia ")
h1, m1, s1 = map(int, input().split(" : "))
d = int(dd[1])
d1 = int(dd1[1])

sp = d*86400 + h * 3600 + m * 60 + s

mg = d1*86400 + h1 * 3600 + m1 * 60 + s1

ds = mg - sp

dt = ds // 86400
ht = ds%86400 // 3600 
mt = ds%3600 // 60
st = ds%60

print(f"{dt} dia(s)")
print(f"{ht} hora(s)")
print(f"{mt} minuto(s)")
print(f"{st} segundo(s)")