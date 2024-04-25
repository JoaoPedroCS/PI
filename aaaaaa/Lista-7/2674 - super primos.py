import math
def is_prime(n):
    if n % 2 == 0 and n != 2 or n ==1:
        return False
    for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True
try:
    while True:
        n = int(input())
        if is_prime(n):
            l = [int(x) for x in str(n) if not is_prime(int(x))]
            if len(l)==0:
                print("Super")
            else:
                print("Primo")
        else:
            print("Nada")
except EOFError:
    exit()