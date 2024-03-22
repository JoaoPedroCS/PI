import math
def teste_de_primo(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = 1000000
l = [2]
for i in range(3, n+1, 2):
    if teste_de_primo(i):
        l.append(i)

print(len(l))