import time
import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True
c = 0
l = []
n =  int(input())
start_time = time.time()
if n%2 == 0:
    n += 1
while c < 10:
    if is_prime(n):
        l.append(n)
        n += 2
        c += 1
    else:
        n += 2
kmh = sum(l)
h = 60000000/kmh
d = h/24
print(f"{kmh:.0f} km/h")
print(f"{int(h)} h / {int(d)} d")
print(f"--- {(time.time() - start_time):.5f} seconds ---")