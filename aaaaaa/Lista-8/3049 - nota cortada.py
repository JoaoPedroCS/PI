b = int(input())
t = int(input())
a = 160*70
area_felix = (b*70 + t*70)/2
area_marzia = a - area_felix
if area_felix > area_marzia:
    print("1")
elif area_felix < area_marzia:
    print("2")
else:
    print("0")