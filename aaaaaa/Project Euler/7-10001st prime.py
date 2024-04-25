import time
start_time = time.time()
import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True
n = 3
l = [2]
while True:
    if is_prime(n):
        l.append(n)
        n += 2
    else:
        n += 2


    if len(l) == 10001:
        print(l)
        break
print(l[-1], "end")
print(f"--- {(time.time() - start_time):.5f} seconds ---")
