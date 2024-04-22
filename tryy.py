import math
def e_primo(m):
    if m % 2 == 0 and m != 2:
        return False
    for x in range(3, math.floor(math.sqrt(m)) + 1, 2):
        if m % x == 0:
            return False
    return True

def no_primo(m):
    if m == 1:
        return 2
    cont = 1
    for x in range(3, 50000000, 2):
        if e_primo(x):
            cont += 1

        if cont == m:
            break
    return x

def diferenca(m1,m2):
    if m1 % 2 != 0:
        m1 += 1
    contagem = 0
    for i in range(m1+1, m2+1, 2):
        if e_primo(i):
            contagem += 1

    return contagem
for i in range(100):
    p1 = no_primo(i)**2
    p2 = no_primo(i+1)**2
    if diferenca(p1,p2) < 4:
        print(f'Problema 1: resultado = {diferenca(p1,p2)}')