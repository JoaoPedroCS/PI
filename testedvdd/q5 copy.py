import math
def teste_de_primo(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

soma_c = 1
q = 1000000
for n in range(3, q+1):
    n_primo = 1
    for i in range(3, n+1, 2):
        if teste_de_primo(i):
            n_primo += 1
    soma_c += n_primo
print(soma_c)