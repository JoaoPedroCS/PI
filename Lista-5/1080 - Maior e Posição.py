x = int(input())
b = x
for i in range(2, 101, 1):
    x = int(input())
    if x > b:
        b = x
        p = i
    
print(b)
print(p)