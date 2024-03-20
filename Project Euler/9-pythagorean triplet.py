def is_square(n):
    sqrt = math.sqrt(n)
    return (sqrt - int(sqrt)) != 0

while True:
    for c in range(499, 332, -1):
        for a in range(332, 0, -1):
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