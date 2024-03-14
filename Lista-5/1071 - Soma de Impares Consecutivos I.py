a = int(input())
b = int(input())
lst = [a,b]
lst.sort()
l = [i for i in range(lst[0]+1, lst[1], 1) if i%2 != 0]
x = sum(l)
print(x)