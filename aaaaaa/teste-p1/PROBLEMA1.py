v = 0
for i in range(6):
    x = input()
    if x == "V":
        v +=1

if 6>= v >=5:
    print("3")
elif 4>= v >=3:
    print("2")
elif 2>= v >=1:
    print("1")
else:
    print("-1")