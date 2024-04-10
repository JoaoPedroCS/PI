import math
def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
def verifica_despojado(n):
    if n == 1:
        return False

    primo = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % (i*i) == 0:
            return False
        if n % i == 0:
            primo = False
    return not primo


n = int(input())
print(verifica_despojado(n))
