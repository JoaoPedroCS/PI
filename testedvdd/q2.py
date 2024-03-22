
h, z , l = map(int, input().split())

if z < h < l or l < h < z:
    print("huguinho")

if h < z < l or l < z < h:
    print("zezinho")

if h < l < z or z < l < h:
    print("luisinho")
