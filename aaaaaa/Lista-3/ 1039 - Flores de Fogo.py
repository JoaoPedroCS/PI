
import math
var = input().split()
try:
    while True:
        r1 = int(var[0])
        x1 = int(var[1])
        y1 = int(var[2])
        r2 = int(var[3])
        x2 = int(var[4])
        y2 = int(var[5])
        x = (x2 - x1) ** 2
        y = (y2 - y1) ** 2
    
        d = math.sqrt(x + y)
    
        if float(r1) < r2:
            print("MORTO")
        elif (r2 + d) <= float(r1):
            print("RICO")
        else:
            print("MORTO")
        var = input().split()
except EOFError:
    exit()