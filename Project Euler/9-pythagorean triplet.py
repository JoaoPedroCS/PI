import time
start_time = time.time()
while True:
    for c in range(499, 333, -1):
        for a in range(293, 0, -1):
            b = 1000 - a - c
            if a**2 + b**2 == c**2:
                break
        if a**2 + b**2 == c**2:
            break
    if a**2 + b**2 == c**2:
        break

print(f"Os fatores são: {a}, {b}, {c}")
print(f"A soma é: {a+b+c}")
print(f"O produto é: {a*b*c}")
print("--- %s seconds ---" % (time.time() - start_time))