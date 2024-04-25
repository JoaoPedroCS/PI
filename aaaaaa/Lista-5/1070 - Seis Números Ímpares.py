a = int(input())

if a%2 == 0:
    x = a+1
else:
    x = a
for i in range(a, a+6, 1):
    print(x)
    x = x + 2