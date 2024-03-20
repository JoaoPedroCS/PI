def my_function(x):
  return x[::-1]
x = 1
while x ==1:
  for i in range(998001, 10000, -1):
    if str(i) == my_function(str(i)):
      for d in range(999, 99, -1):
        if i % d == 0:
          x = 0
          par = i / d
          print(d, par)