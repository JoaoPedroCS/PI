import time
start_time = time.time()
x = 0
y = 1
l = [0]
while y < 4000000:
    z = x
    x = y
    y = z + y
    if y%2==0:
        l.append(y)
print(sum(l))
print(f"--- {(time.time() - start_time):.5f} seconds ---")