import time

def inverse(x):
  return x[::-1]
n = input()
start_time = time.time()
di = "1"
df = "1"
count = 0
for i in range(int(n)):
    df = df + "0"
for i in range(int(n)-1):
    di = di + "0"

for i in range(int(di), int(df)):
   teste = int(inverse(str(i)))
   if teste > i:
      count += 1

print(count)
print(f"--- {(time.time() - start_time):.5f} seconds ---")