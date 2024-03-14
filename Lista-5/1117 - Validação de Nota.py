y = 0
x = 0
while y < 2:
    a = float(input())
    if a < 0 or a > 10:
        print("nota invalida")
    else:
        x += a
        y += 1
print(f"media = {x/2:.2f}")