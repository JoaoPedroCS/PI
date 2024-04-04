import time
n = int(input())
start_time = time.time()
t = 2**n - 1
ti = (t%86400)
h = ti // 3600
m = (ti % 3600) // 60
s = ti % 60

print(f"{h:02d}:{m:02d}:{s:02d}")
print(f"--- {(time.time() - start_time):.5f} seconds ---")