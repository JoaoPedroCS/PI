j = 0.8
i = -0.2
temp = 0
while i < 1.9:
    j += 0.2
    i += 0.2
    x = j + 2
    while j <= x:
        if temp%10 == 0:
            print(F"I={i:.0f} J={j:.0f}")
        else:
            print(F"I={i:.1f} J={j:.1f}")
        j = j + 1
    j = j - 3
    temp +=2