import time
start_time = time.time()
l = [i for i in range(1, 1000) if i%3==0 or i%5==0]
print(sum(l))

print(f"--- {(time.time() - start_time):.5f} seconds ---")