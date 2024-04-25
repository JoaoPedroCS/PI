import time
start_time = time.time()
def inverse(x):
  return x[::-1]

def no_digits(n):
  count=0
  while(n>0):
      count += 1
      n=n//10
  return count

x = 1
while x == 1:
  for i in range(998001, 10000, -1):
    if str(i) == inverse(str(i)):
      for d in range(999, 99, -1):
        if i % d == 0 and no_digits(i/d) == 3:
          par = i / d
          print(d, par)
          print(i)
          x = 0
          break
    if x == 0:
      break
print(f"--- {(time.time() - start_time):.5f} seconds ---")