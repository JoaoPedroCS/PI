n = int(input())
lst = [0]
for i in range(0, n, 1):
    x = int(input())
    lst.append(x)
i = [y for y in lst if 10<=y<=20]
ni = len(i)
print(f"{ni} in")
print(f"{n-ni} out")