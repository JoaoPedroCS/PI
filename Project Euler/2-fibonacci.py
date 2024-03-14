x = 0
y = 1
l = [0]
while y < 4000000:
    z = x
    x = y
    y = z + y
    if y%2==0:
        l.append(y)
    print(l)
print(sum(l))